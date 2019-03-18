# -*- coding: utf-8 -*-
__author__ = 'panchao'

import django_filters
from .models import Banner


class BannerFilter(django_filters.rest_framework.FilterSet):
    product_name = django_filters.CharFilter(field_name="product_name", lookup_expr="exact")

    class Meta:
        model = Banner
        fields = ['id']