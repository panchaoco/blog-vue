# -*- coding: utf-8 -*-
__author__ = 'panchao'

from rest_framework import serializers
from .models import Comment


class CommentChildrenSerializer(serializers.ModelSerializer):
    comment_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    username = serializers.CharField(source='user.username', required=False)
    # user_id = serializers.IntegerField(source='user.id', required=False)
    top_img = serializers.CharField(source='user.top_img', required=False)

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    comment_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # 通过当前model的外键名指向外键model对应的属性可以获取到外键内容
    username = serializers.CharField(source='user.username', required=False)
    # user_id = serializers.IntegerField(source='user.id', required=False)
    top_img = serializers.CharField(source='user.top_img', required=False)
    children = CommentChildrenSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'
