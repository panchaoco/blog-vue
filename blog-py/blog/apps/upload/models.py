from datetime import datetime
from django.db import models
from article.models import BlogArticle
from .storage import ImageStorage

# Create your models here.


class Upload(models.Model):
    image = models.ImageField(max_length=500, upload_to='article/', storage=ImageStorage())

    add_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    class Meta:
        verbose_name = '图片上传'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image