from django.urls import path

from .views import MainView, PostView

urlpatterns = [
    path("", MainView.as_view()),
    path("post/", PostView.as_view()),
]
