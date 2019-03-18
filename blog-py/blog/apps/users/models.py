from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=16, null=True, blank=True, verbose_name="用户名")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    top_img = models.ImageField(max_length=200, null=True, upload_to="user/")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
