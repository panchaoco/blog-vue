from datetime import datetime
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth import get_user_model
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.settings import api_settings

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

from .serializers import UserRegSerializer
from common_data.serializer_data import success, error
# Create your views here.

User = get_user_model()


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegSerializer

    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user else user.username
        re_dict["user_id"] = user.id
        re_dict["is_super_user"] = user.is_superuser if user.is_superuser else 0
        data = success(data=re_dict)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    # 重载perform_create
    def perform_create(self, serializer):
        return serializer.save()

