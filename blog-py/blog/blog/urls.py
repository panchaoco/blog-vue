"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from blog.settings import MEDIA_ROOT
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve

from article.views import BlogArticleViewSet, CategoryViewSet, BlogDomain
from users.views import UserViewSet
from users.verifycode import get_valid_img
from comment.views import CommentViewGet, CommentViewSet
from music.views import get_music_list, get_music_play_url, get_music_album, get_music_lyric, MusicView
from banner.views import BannerView

from upload.views import UploadViewSet

router = DefaultRouter()

router.register(r'v1/api/register', UserViewSet, base_name="注册")
router.register(r'v1/api/article', BlogArticleViewSet, base_name="获取文章列表")
router.register(r'v1/api/comment', CommentViewGet, base_name="获取评论列表")
router.register(r'v1/api/add_comment', CommentViewSet, base_name="添加评论")
router.register(r'v1/api/upload', UploadViewSet, base_name="上传图片")
router.register(r'v1/api/category', CategoryViewSet, base_name="新增分类")
router.register(r'v1/api/banner', BannerView, base_name="轮播图")
router.register(r'v1/api/blog_info', BlogDomain, base_name="文章的汇总信息")
router.register(r'v1/api/music_date', MusicView, base_name="请求qq音乐的时间")
urlpatterns = [
    # path('admin/', admin.site.urls),
    url('^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^v1/api/login/', obtain_jwt_token),
    url(r'v1/api/code/', get_valid_img),
    url(r'v1/api/get_music_list/', get_music_list),
    url(r'v1/api/get_music_play_url/', get_music_play_url),
    url(r'v1/api/get_music_play_album/', get_music_album),
    url(r'v1/api/get_music_lyric/', get_music_lyric),
]
