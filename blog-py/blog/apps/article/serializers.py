# -*- coding: utf-8 -*-
__author__ = 'panchao'

from rest_framework import serializers

from article.models import BlogArticle, Category


class BlogArticleSerializers(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = BlogArticle
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_category = CategorySerializer2(many=True, required=False)
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Category
        fields = "__all__"


