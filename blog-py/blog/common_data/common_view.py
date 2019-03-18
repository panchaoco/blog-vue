# -*- coding: utf-8 -*-
__author__ = 'panchao'
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer_data import success, error


class ModelViewSet(viewsets.ModelViewSet):

    # def get_authenticators(self):
    #     """
    #     Instantiates and returns the list of authenticators that this view can use.
    #     """
    #     if self.request.method.lower() != 'get' and self.request.GET.get('look_count') != None:
    #         self.authentication_classes = (JSONWebTokenAuthentication, )
    #     return [auth() for auth in self.authentication_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(success(data=serializer.data, message="添加成功"), status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        # 重写list方法
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(success(data=serializer.data))

        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response(data=success(serializer.data[0] if self.request.query_params.get("id") else serializer.data))
        else:
            return Response(data=success([]))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        message = '操作成功'
        return Response(data=success(data=[], message=message))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data=success(data=[]), status=status.HTTP_200_OK)
