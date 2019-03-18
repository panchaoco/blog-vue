# -*- coding: utf-8 -*-
__author__ = 'panchao'

import django_filters
from .models import BlogArticle, Category


class ArticleFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    article_type = django_filters.CharFilter(field_name='article_type', lookup_expr='exact')
    is_hot = django_filters.NumberFilter(field_name='is_hot', lookup_expr='exact')

    class Meta:
        model = BlogArticle
        fields = ['id', 'article_type', 'is_hot']


class CategoryFilter(django_filters.rest_framework.FilterSet):
    category_type = django_filters.NumberFilter(field_name='category_type', lookup_expr='exact')

    class Meta:
        model = Category
        fields = ['category_type']