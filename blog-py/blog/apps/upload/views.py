from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Upload
from .serializers import UploadSerializer
from common_data.serializer_data import success

# Create your views here.


class UploadViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(success(data=serializer.data, message='上传成功'), status=status.HTTP_201_CREATED, headers=headers)


