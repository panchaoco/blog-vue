# -*- coding: utf-8 -*-
__author__ = 'panchao'
import random
from common_data.serializer_data import success


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return success(data={
        'token': token,
        'user_id': user.id,
        'username': user.username,
        'is_super_user': user.is_superuser
    }, message="登录成功")


# 获取随机颜色
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)
