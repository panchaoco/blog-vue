<template>
  <section class="music-play-container" :style="bgRgb">
    <div class="music-pic-wrapper">
      <div class="music-info">
        <div class="play-list">
          <ul>
            <li v-for="(item, index) in playList" :key="index" :style="{borderBottom: `1px solid ${border}`}">
              <div class="info">
                <span>{{item.songname}}</span>
                <i style="margin: 0 6px">-</i>
                <p class="single" v-for="(s_item, i) in item.singer" :key="s_item.id">
                  <span>{{s_item.name}}</span>
                  <span style="margin: 0 6px">{{i !== item.singer.length - 1 ? '-' : ''}}</span>
                </p>
              </div>
              <div class="play-status" title="播放">
                <Icon type="md-play"/>
              </div>
              <div class="dynamic">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
              </div>
              <div class="remove" title="删除">
                <Icon type="md-trash"/>
              </div>
            </li>
          </ul>
        </div>
        <div class="music">
          <div class="pic-border" ref="border" :class="{begin: begin, hidden: hide}" @click="togglePlayStatus">
            <img :src="pic" alt="">
          </div>
          <div class="lyric-wrapper">
            <div class="lyric" :style="{transform: `translateY(${top}px)`}">
              <p ref="lyric" v-for="(ly, index) in lyricArr" :key="index" :class="{active: currentLyric === index}">
                {{ly.text}}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="programs">
        <span class="begin-time">{{handleMusicTime(beginTime)}}</span>
        <div class="line"></div>
        <span class="duration">{{handleMusicTime(endTime)}}</span>
        <div class="play-list-icon" @click="onPlayList">
          <Icon type="md-reorder"/>
        </div>

      </div>
    </div>
    <audio ref="audio" :src="playUrl[0]" v-if="playUrl.length > 0" preload @canplay="canPlay" @ended="onEnded">
      <source :src="url" v-for="(url, index) in playUrl" :key="index"/>
    </audio>
    <div class="player-img" :style="{backgroundImage: `url(${pic})`}"></div>
  </section>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  import {Base64} from 'js-base64';
  import cookie from '../../utils/music/cookie'
  import getGuid from '../../utils/music/guid'
  import musicKey from '../../utils/music/music_key'

  export default {
    name: "MusicPlay",
    data() {
      return {
        pic: '',
        begin: false,
        hide: false,
        show: false,
        beginTime: 0,
        endTime: 0,
        currentPlay: Number(window.localStorage.getItem('currentPlay')) || 0,
        lyricArr: [],
        params: {
          guid: getGuid(),
          songmid: [],
          songtype: [0],
          uin: "0",
          loginflag: 1,
          platform: "20"
        },
        playGetData: {
          req: {
            module: 'CDN.SrfCdnDispatchServer',
            method: 'GetCdnDispatch',
            param: {guid: getGuid(), calltype: 0, userip: ''}
          },
          req_0: {
            module: 'vkey.GetVkeyServer',
            method: 'CgiGetVkey',
            param: this.params
          },
          comm: {
            uin: 0,
            format: 'json',
            ct: 24,
            cv: 0
          }

        },
        playList: JSON.parse(window.localStorage.getItem('playList')),
        playUrl: '',
        audio: null,
        openList: false,
        bgRgb: null,
        currentLyric: 0,
        top: 0
      }
    },
    computed: {
      ...mapState({
        musicOpt: state => state.music.musicOpt,
        play: state => state.music.play,
      }),
    },
    created() {
      this.rgbStyle()
      window.addEventListener('storage', (e) => {
        if (e.key === 'playList' && e.newValue !== e.oldValue) {
          this.top = 0
          this.playList = JSON.parse(e.newValue)
          this.init()
          this.rgbStyle()
        }
      }, false)
    },
    mounted() {
      this.$nextTick(() => {
        this.init()
        this.show = true
      })
    },
    methods: {
      ...mapMutations({
        updateSongUrl: 'music/updateSongUrl',
        updatePlayStatus: 'music/updatePlayStatus',
        updateMusicPic: 'music/updateMusicPic',
        updateMusicAlbumMid: 'music/updateMusicAlbumMid'
      }),
      init() {
        this.getAlbum()
        this.getLyric()
      },
      getAlbum() {
        const g_tk = cookie.getACSRFToken()
        const album_mid = this.playList[this.currentPlay].albummid
        this.$store.dispatch('music/getMusicAlbum', {
          ct: 24,
          g_tk,
          albummid: album_mid
        }).then(res => {
          if (res.code === 0) {
            this.pic = `https://y.gtimg.cn/music/photo_new/T002R300x300M000${res.data.mid}.jpg?max_age=${Math.ceil(Math.random() * 3000000)}`
            this.updatePlayStatus(true)
            this.begin = true
          }
        })
      },
      getLyric() {
        const g_tk = cookie.getACSRFToken()
        if (this.playList && this.playList.length > 0) {
          this.$store.dispatch('music/getMusicLyric', {
            '-': 'MusicJsonCallback_lrc',
            pcachetime: (new Date()).valueOf(),
            songmid: this.playList[this.currentPlay].songmid,
            g_tk
          }).then(res => {
            if (res.code === 0) {
              this.lyricArr = []
              const lyric = Base64.decode(res.lyric)
              lyric.split(/\n/).forEach(ly => {
                const reg = /\[\d{2}.*\]/g
                const match = ly.match(reg)
                if (match && !!ly.split(reg)[1]) {
                  this.lyricArr.push({
                    time: match[0].replace('[', '').replace(']', '').split('.')[0],
                    text: ly.split(reg)[1]
                  })
                }
              })
            }
            this.getPlayUrl()
          })
        }
      },
      getPlayUrl() {
        this.$set(this.params, 'songmid', [this.playList[this.currentPlay].songmid])
        this.$set(this.params, 'songtype', [this.playList[this.currentPlay].songtype])
        this.playGetData.req_0.param = this.params
        this.$store.dispatch('music/getMusicPlayUrl', {
          "-": musicKey,
          "g_tk": cookie.getACSRFToken(),
          "loginUin": 0,
          "hostUin": 0,
          "format": "json",
          "inCharset": "utf8",
          "outCharset": "utf-8",
          "notice": 0,
          "platform": "yqq.json",
          "needNewCode": 0,
          data: JSON.stringify(this.playGetData)
        }).then(res => {
          const data = res.req_0.data
          const req = res.req.data
          const item = this.playList[this.currentPlay]
          const domain = req.freeflowsip && req.freeflowsip.length > 0 ? req.freeflowsip[0] : data.sip[0]
          item.play = !item.play
          let playUrl = []
          if (data.midurlinfo.length > 0) {
            const purl = !!data.midurlinfo[0].purl ? data.midurlinfo[0].purl : data.testfile2g
            const url = `${domain}${purl}`
            playUrl = [url]
          }
          const sip = req.sip
          sip.forEach(s => {
            playUrl.push(`${s}${req.testfile2g}&r=${(Math.random()).toString().replace('0.', '')}`)
          })
          this.playUrl = playUrl
        })
      },
      togglePlayStatus() {
        this.$refs.border.style.animationPlayState = this.play ? 'paused' : 'running'
        this.updatePlayStatus(!this.play)

      },
      getMusicInfo(audio = this.audio) {
        this.endTime = parseInt(audio.duration)
      },
      currentPlayTime() {
        setTimeout(() => {
          this.beginTime++
          if (this.beginTime <= this.endTime) {
            for (let i = 0; i < this.lyricArr.length; i++) {
              if (i < this.lyricArr.length - 1) {
                const prev = this.lyricArr[i].time.split(':')
                const next = this.lyricArr[i + 1].time.split(':')
                if (this.beginTime >= parseInt(prev[0] * 60) + parseInt(prev[1]) &&
                  this.beginTime <= parseInt(next[0] * 60) + parseInt(next[1])
                ) {
                  this.currentLyric = i
                }
              }
            }
            this.currentPlayTime()
          }
        }, 1000)
      },
      playMusic() {
        this.audio = this.$refs.audio
        this.audio.play()
      },
      rgbStyle() {
        let r = Math.ceil(Math.random() * 255)
        let g = Math.ceil(Math.random() * 255)
        let b = Math.ceil(Math.random() * 255)
        r = r < 100 ? 100 : r
        g = g < 120 ? 120 : g
        b = b < 150 ? 150 : b
        this.border = `rgba(${r + 20}, ${g}, ${b + 30}, 0.2)`
        this.bgRgb = {
          background: `linear-gradient(to right, rgba(${r + 20}, ${g}, ${b + 40}, 1), rgba(${r + 10}, ${g - 40}, ${b + 30}, 1), rgba(${r + 30}, ${g}, ${b + 50}, 1))`
        }
      },
      onEnded() {

      },
      canPlay() {
        this.$nextTick(() => {
          this.playMusic()
          this.getMusicInfo()
          this.currentPlayTime()
        })
      },
      onPlayList() {
        this.openList = !this.openList
      },
      handleMusicTime(time) {
        const m = Math.floor(time / 60)
        const s = time - m * 60 < 10 ? `0${time - m * 60}` : time - m * 60
        return `0${m}:${s}`
      }
    },
    watch: {
      currentLyric(val, old) {
        if (val !== old && val >= 6 && this.lyricArr.length - 6 >= val) {
          this.top = -(30 * (val - 6))
        }
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "./MusicPlay";

</style>
