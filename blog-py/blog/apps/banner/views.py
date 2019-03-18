from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from common_data import common_view
from .models import Banner
from .serializers import BannerSerializer
from .filters import BannerFilter
# Create your views here.


class BannerView(common_view.ModelViewSet):

    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = BannerFilter
