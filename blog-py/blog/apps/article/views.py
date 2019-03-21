from django.shortcuts import render
from rest_framework import mixins, viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.core.paginator import InvalidPage
from django.utils import six
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict, namedtuple
from .models import BlogArticle, Category
from comment.models import Comment
from .serializers import BlogArticleSerializers, CategorySerializer
from .filters import ArticleFilter, CategoryFilter
from common_data import common_view
from utils.permissions import IsOwnerOrReadOnly

from common_data.serializer_data import success, error

# Create your views here.
User = get_user_model()


class BlogArticlePagination(PageNumberPagination):
  page_size_query_param = 'page_size'
  page_query_param = 'page'

  def get_paginated_response(self, data):
    new_data = {
      "page": {
        "total": self.page.paginator.count,
        "page_size": self.get_page_size(self.request),
        "page": int(self.request.query_params.get(self.page_query_param, 1))
      },
    }
    dict_data = dict(data)
    dict_data.update(new_data)
    return Response(dict_data)


class BlogArticleViewSet(common_view.ModelViewSet):
  """
  添加文章
  """
  queryset = BlogArticle.objects.all()
  serializer_class = BlogArticleSerializers
  pagination_class = BlogArticlePagination
  filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
  filter_class = ArticleFilter
  search_fields = ('title',)
  ordering_fields = ('update_time', 'add_time')


class CategoryViewSet(common_view.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filter_backends = (DjangoFilterBackend,)
  filter_class = CategoryFilter


class BlogDomain(common_view.ModelViewSet):

  def list(self, request, *args, **kwargs):
    code_len = len(BlogArticle.objects.filter(article_type=1))
    essay_len = len(BlogArticle.objects.filter(article_type=2))
    category_len = len(Category.objects.all())

    return Response(success(data={
      "code_len": code_len,
      "essay_len": essay_len,
      "category_len": category_len
    }))


def getArticleData(request):
  articles = BlogArticle.objects.all()
  return render(request, 'index.html', {'articles': articles})

