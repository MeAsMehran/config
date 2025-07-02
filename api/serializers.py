from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        # 2 code lines below are the same!
        # fields = ("title", "slug", "author", "content", "publish", "status",)     # you can also work with lists ["title", ...]
        # exclude = ("created", "updated")        # you can also work with lists ["title", ...] | exclude select all field except those were mentioned
        # fields = "__all__"                        # this will make all fields selected
        exclude = ("created", "updated")



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
