from rest_framework import serializers

from orm.models import Post, Category, Comment, Profile


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    author_username = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Post
        fields = ["id", "title", "content", "header_image",
                  "snippet", "category", "author",
                  "category_name", "author_username"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "name", "body"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "website", "bio", "phone", "profile_image", "github"]