from django.urls import path

from orm.views import list_posts

urlpatterns = [
    path("list_posts/", list_posts, name="list_posts"),
]