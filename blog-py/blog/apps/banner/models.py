from datetime import datetime
from django.db import models

# Create your models here.


class Banner(models.Model):
    product_name = models.CharField(max_length=10, null=True, blank=True, verbose_name="归属产品", help_text="归属产品")
    image = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片地址", help_text="图片地址")
    pid = models.IntegerField(null=True, blank=True, verbose_name="关联ID", help_text="关联ID")
    link = models.TextField(null=True, blank=True, verbose_name="链接", help_text="链接")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image