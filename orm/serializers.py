from django.contrib.auth.models import User
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

    def create(self, validated_data):
        print(self.context)
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True
            }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


