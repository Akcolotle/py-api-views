from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreView, ActorView, MovieViewSet, CinemaHallViewSet

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema-halls", CinemaHallViewSet)

urlpatterns = [
    path("genres/", GenreView.as_view()),
    path("genres/<int:pk>/", GenreView.as_view()),
    path("actors/", ActorView.as_view()),
    path("actors/<int:pk>/", ActorView.as_view()),
    path("", include(router.urls)),
]
