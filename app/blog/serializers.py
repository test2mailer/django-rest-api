from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Category, Tag, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


"""Post API"""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "category", "tags", "image", "status", 'pub_date', 'created_on']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "description"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]
