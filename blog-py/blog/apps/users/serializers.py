# -*- coding: utf-8 -*-
__author__ = 'panchao'

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True, allow_blank=False, label="用户名",
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")]
                                     )
    # is_super_user = serializers.BooleanField(required=False)

    password = serializers.CharField(
        style={'input_type': 'password'},
        label="密码",
        write_only=True,
    )

    class Meta:
        model = User
        fields = ("username", "password")
