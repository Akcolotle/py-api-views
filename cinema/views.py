from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from django.shortcuts import get_object_or_404

from cinema.models import Genre, Actor, Movie, CinemaHall
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    CinemaHallSerializer,
)


class GenreView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)

        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(
            genre, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        get_object_or_404(Genre, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorView(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk=None):
        if pk is None:
            serializer = self.get_serializer(
                self.get_queryset(), many=True
            )
            return Response(serializer.data)

        actor = self.get_object()
        serializer = self.get_serializer(actor)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        actor = self.get_object()
        serializer = self.get_serializer(actor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        actor = self.get_object()
        serializer = self.get_serializer(
            actor, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
