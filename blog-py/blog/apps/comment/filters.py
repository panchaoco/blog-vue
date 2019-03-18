# -*- coding: utf-8 -*-
__author__ = 'panchao'

import django_filters
from .models import Comment


class CommentFilter(django_filters.rest_framework.FilterSet):
    article_id = django_filters.NumberFilter(field_name='article_id', lookup_expr='exact')

    class Meta:
        model = Comment
        fields = ['article_id']