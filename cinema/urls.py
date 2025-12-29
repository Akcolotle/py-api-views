from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    MovieList, MovieDetail,
    CinemaHallViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),

    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),

    path("movies/", MovieList.as_view()),
    path("movies/<int:pk>/", MovieDetail.as_view()),

    path("", include(router.urls)),
]
