# Generated by Django 2.1.4 on 2019-02-21 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(max_length=500, upload_to='article/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '图片上传',
                'verbose_name_plural': '图片上传',
            },
        ),
    ]