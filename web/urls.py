from django.urls import path
from .views import (
    HomeView,
    PostsView,
    PostDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/", PostsView.as_view(), name="posts"),
    path("posts/create/", CreatePostView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", UpdatePostView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", DeletePostView.as_view(), name="post_delete"),
]
