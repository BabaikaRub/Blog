from django.urls import path

from .views import MainView, PostDetailView

urlpatterns = [
    path("", MainView.as_view()),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
