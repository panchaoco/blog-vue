# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Banner

__author__ = 'panchao'


class BannerSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Banner
        fields = "__all__"

