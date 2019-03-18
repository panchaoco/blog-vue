from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from .models import Comment
from .serializers import CommentSerializers
from .filters import CommentFilter
from common_data.serializer_data import success, error
# Create your views here.

User = get_user_model()


class CommentViewGet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.filter(comment_type=1)
    serializer_class = CommentSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        return Response(success(data=serializer.data))


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CommentSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(success(data=[]), status=status.HTTP_201_CREATED, headers=headers)