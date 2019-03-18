from django.shortcuts import render, HttpResponse

from django.http import JsonResponse

from django.contrib import auth
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO
from rest_framework.response import Response
from rest_framework.decorators import api_view
import hashlib

import base64


# Create your views here.


# 自己生成验证码的登录

def login(request):
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        valid_code = request.POST.get("valid_code")  # 获取用户填写的验证码
        if valid_code and valid_code.upper() == request.session.get("valid_code", "").upper():
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login.html")


# 获取验证码图片的视图
@api_view(['GET', 'POST', ])
def get_valid_img(request):
    # 获取随机颜色的函数
    def get_random_color(begin_rgb=0, end_rgb=255):
        return random.randint(begin_rgb, end_rgb), random.randint(begin_rgb, end_rgb), random.randint(begin_rgb, end_rgb)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color(begin_rgb=160)
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype(r'static/arial.ttf', 36)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(4):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20 + 40 * i, 0), tmp, fill=get_random_color(begin_rgb=10, end_rgb=66), font=font_obj)

    # 保存到session

    font_utf8 = "".join(tmp_list).encode("utf-8")
    font_md5 = hashlib.md5(font_utf8).hexdigest()
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    width = 190  # 图片宽度（防止越界）
    height = 35
    for i in range(4):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=get_random_color())

    # 加干扰点
    for i in range(40):
        draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    base = base64.b64encode(data)
    return Response({
        "state": 0,
        "message": "获取成功",
        "data": {
            "token": font_md5,
            "img": ''.join(['data:image/jpg;base64,', base.decode("utf-8")])
        }
    }, status=200)

