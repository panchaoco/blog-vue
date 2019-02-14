import Axios from '../../utils/Axios'
export default {
  namespace: 'music',
  state: {
    play: false,
    songList: [],
    currentMusicPic: '',
    musicOpt: {
      currentMusicPic: '',
      current_song_url: '',
      album_mid: '',
      current: -1,
    },
    audio: null
  },
  mutations: {
    ['music/updateSongUrl'](state, {url, index}) {
      state.musicOpt.current_song_url = url
      state.musicOpt.current = index
      state.songList.push({
        song_url: url,
        id: index
      })
    },
    ['music/updatePlayStatus'](state, status) {
      state.play = status
    },
    ['music/updateMusicPic'](state, pic) {
      state.musicOpt.currentMusicPic = pic
    },
    ['music/updateMusicAlbumMid'](state, mid) {
      state.musicOpt.album_mid = mid
    },
    ['music/updateAudio'](state, audio) {
      state.audio = audio
    }
  },
  actions: {
    async ['music/getMusicComment']({commit}, payload) {
      const res = await Axios('/api/v1/get_music_list/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['music/getMusicPlayUrl']({commit}, payload) {
      const path = '/cgi-bin/musicu.fcg?'
      let str = ''
      for (let key in payload) {
        str += `${key}=${key === 'data' ? escape(payload[key]) : payload[key]}&`
      }
      str = str.substring(0, str.length - 1)
      const headerPath = `${path}${str}`
      payload[':path'] = headerPath
      const res = await Axios('/api/v1/get_music_play_url/', {
        method: 'GET',
        body: payload,
      })
      return res
    },
    async ['music/getMusicAlbum']({commit}, payload) {
      const res = await Axios('/api/v1/get_music_play_album/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['music/getMusicLyric']({commit}, payload) {
      const res = await Axios('/api/v1/get_music_lyric/', {
        method: 'GET',
        body: payload
      })
      return res
    }
  }
}
