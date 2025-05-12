from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from orm.models import Post
from orm.serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def list_posts(request):
    posts = Post.objects.all()
    posts_serializers = PostSerializer(posts, many=True)
    return Response(posts_serializers.data)


@api_view(['GET'])
def logout(request):
    user = request.user
    user.auth_token.delete()
    return Response({"message": "logout Successfully"})