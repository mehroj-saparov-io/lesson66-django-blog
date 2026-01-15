import json
import os
from datetime import datetime

from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.utils.text import slugify

from .forms import PostCreationForm, PostUpdateForm


# posts.txt - ma'lumotlar fayli
POSTS_FILE = os.path.join(settings.BASE_DIR, "posts.txt")



def load_data():
    if not os.path.exists(POSTS_FILE):
        return []
    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(posts):
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")


# viewlar

class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        posts = load_data()

        posts = sorted(
            posts,
            key=lambda p: parse_date(p["created_at"]),
            reverse=True
        )

        return render(request, "home.html", {
            "latest_posts": posts[:2]
        })


class PostsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        posts = load_data()

        # filter: published / unpublished
        status = request.GET.get("status")
        if status == "published":
            posts = [p for p in posts if p.get("is_published")]
        elif status == "unpublished":
            posts = [p for p in posts if not p.get("is_published")]

        # search
        query = request.GET.get("q", "").lower()
        if query:
            posts = [
                p for p in posts
                if query in p["title"].lower()
                or query in p["content"].lower()
            ]

        posts = sorted(
            posts,
            key=lambda p: parse_date(p["created_at"]),
            reverse=True
        )

        return render(request, "posts.html", {
            "posts": posts,
            "status": status,
            "query": query,
        })


class PostDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        posts = load_data()
        post = next((p for p in posts if p["slug"] == slug), None)

        if not post:
            raise Http404("Post topilmadi")

        return render(request, "post_detail.html", {"post": post})


class CreatePostView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = PostCreationForm()
        return render(request, "create_post.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = PostCreationForm(request.POST)

        if form.is_valid():
            posts = load_data()
            posts.append(form.cleaned_data)
            save_data(posts)
            return render(request, "post_created.html")

        return render(request, "create_post.html", {"form": form})


class UpdatePostView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        posts = load_data()
        post = next((p for p in posts if p["slug"] == slug), None)

        if not post:
            raise Http404("Post topilmadi")

        form = PostUpdateForm(initial={
            "title": post["title"],
            "content": post["content"],
            "is_published": post["is_published"],
        })

        return render(request, "update_post.html", {
            "form": form,
            "post": post,
        })

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        posts = load_data()
        post = next((p for p in posts if p["slug"] == slug), None)

        if not post:
            raise Http404("Post topilmadi")

        form = PostUpdateForm(request.POST)

        if form.is_valid():
            post["title"] = form.cleaned_data["title"]
            post["content"] = form.cleaned_data["content"]
            post["is_published"] = form.cleaned_data["is_published"]
            post["updated_at"] = form.cleaned_data["updated_at"]

            save_data(posts)

            return redirect("post_detail", slug=post["slug"])


            save_data(posts)
            return render(request, "post_updated.html")

        return render(request, "update_post.html", {
            "form": form,
            "post": post,
        })


class DeletePostView(View):
    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        posts = load_data()
        posts = [p for p in posts if p["slug"] != slug]
        save_data(posts)
        return redirect("posts")
