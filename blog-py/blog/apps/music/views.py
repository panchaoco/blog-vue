from .common import GetMusicList
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

from common_data import common_view
from .models import Music
from .serializers import MusicSerializer


class MusicView(common_view.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


@api_view(['GET'])
def get_music_list(request):

    music = GetMusicList()

    return JsonResponse(music.get_music(request), safe=False)


@api_view(['GET'])
def get_music_play_url(request):

    music = GetMusicList()

    return JsonResponse(music.get_music_play_url(request), safe=False)


@api_view(['GET'])
def get_music_album(request):

    music = GetMusicList()

    return JsonResponse(music.get_music_album(request), safe=False)


@api_view(['GET'])
def get_music_lyric(request):

    music = GetMusicList()

    return JsonResponse(music.get_music_lyric(request), safe=False)