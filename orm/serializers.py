from rest_framework import serializers

from orm.models import Post


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(sourcge="category.name")
    author_username = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Post
        fields = ["id", "title", "content", "header_image",
                  "snippet", "category", "author",
                  "category_name", "author_username"]