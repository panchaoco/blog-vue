# -*- coding: utf-8 -*-
__author__ = 'panchao'


def success(data=[], message='操作成功'):
    re_dict = {}
    re_dict["state"] = 0
    re_dict["message"] = message
    re_dict["data"] = data
    return re_dict


def error(data=[], message='操作失败'):
    re_dict = {}
    re_dict["state"] = 0
    re_dict["message"] = message
    re_dict["data"] = data
    return re_dict
