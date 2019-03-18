# -*- coding: utf-8 -*-
__author__ = 'panchao'

from rest_framework import serializers

from .models import Upload


class UploadSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Upload
        fields = ("image", 'add_time', )