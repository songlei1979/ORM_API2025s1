from django.urls import path
from rest_framework.routers import DefaultRouter
from orm.viewsets import PostViewSet, CategoryViewSet, ProfileViewSet, CommentViewSet, UserViewSet
from orm.views import list_posts
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'comments', CommentViewSet)
router.register('users', UserViewSet)
urlpatterns = router.urls

urlpatterns.append(path("list_posts/", list_posts, name="list_posts"))