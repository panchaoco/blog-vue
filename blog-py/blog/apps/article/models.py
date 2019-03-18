from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class BlogArticle(models.Model):
    """
    博客文章
    """
    ARTICLE_TYPE = (
        (1, "技术"),
        (2, "随记"),
    )
    ORIGINAL = (
        (1, "原创"),
        (2, "转载"),
    )
    title = models.CharField(max_length=100, null=False, blank=True, verbose_name="文章标题", help_text="文章标题")
    img_src = models.CharField(max_length=300, null=True, blank=True, verbose_name="文章图片", help_text="文章图片")
    content = models.TextField(default="", verbose_name="文章内容", help_text="文章内容")
    markdown = models.TextField(default="", verbose_name="文章Markdown内容", help_text="文章Markdown内容")
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name="文章简介", help_text="文章简介")
    thumbs_up_count = models.IntegerField(null=True, default=10, blank=True, verbose_name="点赞人数", help_text="点赞人数")
    share_count = models.IntegerField(null=True, blank=True, default=10, verbose_name="分享次数", help_text="分享次数")
    look_count = models.IntegerField(null=True, blank=True, default=10, verbose_name="已看人数", help_text="已看人数")
    comment_count = models.IntegerField(null=True, blank=True, default=10, verbose_name="评论条数", help_text="评论条数")
    is_hot = models.IntegerField(null=True, blank=True, default=0, verbose_name="是否热门", help_text="是否热门")
    category_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="文章分类", help_text="文章分类")
    add_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name="更新时间")
    article_type = models.IntegerField(choices=ARTICLE_TYPE, default=1, verbose_name="文章类型", help_text="文章类型")
    original = models.BooleanField(default=True, verbose_name="是否原创", help_text="是否原创")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="分类名称", help_text="分类名称")
    add_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name="创建时间")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_category")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name