from datetime import datetime
from django.db import models

# Create your models here.


class Music(models.Model):
    add_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name="创建时间")
    get_music_date = models.CharField(max_length=10, default="2019_05", blank=True, verbose_name="请求音乐时间")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_music_date