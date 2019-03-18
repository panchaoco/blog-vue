# -*- coding: utf-8 -*-
__author__ = 'panchao'
import requests
import random
import json


class GetMusicList:
    """
    qq音乐
    """
    def __init__(self):
        self.headers = {
            "origin": "https://y.qq.com",
            "referer": "https://y.qq.com"
        }
        self.common_params = {
            "loginUin": 0,
            "hostUin": 0,
            "format": "json",
            "inCharset": "utf8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "yqq.json",
            "needNewCode": 0,
        }

    def get_music(self, request):
        """
        返回QQ音乐的数据
        """
        url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg"
        private_params = {
            "tpl": 3,
            "page": "detail",
            "topid": 26,
            "type": "top",
        }

        params = dict(private_params)
        params.update(self.common_params)
        params.update({
            "g_tk": request.GET.get("g_tk"),
            "song_begin": request.GET.get("song_begin"),
            "song_num": request.GET.get("song_num"),
            "date": request.GET.get("date") if request.GET.get("date") else "2019_05"
        })

        wb_data = requests.get(url=url, headers=self.headers, params=params)
        data = wb_data.json()
        return data

    def get_music_play_url(self, request):
        # 获取播放地址
        url = "https://u.y.qq.com/cgi-bin/musicu.fcg"
        gets = request.GET
        headers = {
            "origin": "https://y.qq.com",
            "referer": "https://y.qq.com/portal/player.html",
            # "authority": "u.y.qq.com",
            # "method": "GET",
            # "scheme": "https"
        }
        http_params = {
            "-": gets.get("-"),
            "g_tk": gets.get("g_tk"),
            "data": gets.get("data")
        }
        params = dict(http_params)
        params.update(self.common_params)
        url_data = requests.get(url=url, headers=headers, params=params)
        return url_data.json()

    def get_music_album(self, request):
        # 获取播放专辑详情
        url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg"
        headers = {
            "origin": "https://y.qq.com",
            "referer": "https://y.qq.com/portal/player.html",
        }
        http_params = {
            "ct": request.GET.get('ct'),
            "g_tk": request.GET.get('g_tk'),
            "albummid": request.GET.get('albummid'),
        }
        params = dict(http_params)
        params.update(self.common_params)
        data = requests.get(url, headers=headers, params=params)
        return data.json()

    def get_music_lyric(self, request):
        # 获取歌词
        url = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg"

        headers = {
            "origin": "https://y.qq.com",
            "referer": "https://y.qq.com/portal/player.html",
        }

        http_params = {
            "-": request.GET.get('-'),
            "songmid": request.GET.get('songmid'),
            "pcachetime": request.GET.get('pcachetime'),
        }

        params = dict(http_params)
        params.update(self.common_params)
        data = requests.get(url, headers=headers, params=params)
        return data.json()
