<template>
  <section class="music-play-container">
    <div class="music-pic-wrapper">
      <div class="music-info">
        <div class="play-list">
          <ul class="top">
            <li>
              <div class="title">歌曲信息</div>
              <div class="profile">操作</div>
              <div class="status">状态</div>
              <div class="del">删除</div>
            </li>
          </ul>
          <div class="scroll">
            <swiper :options="swiperOption">
              <swiper-slide class="text">
                <ul class="list content">
                  <li v-for="(item, index) in playList" :key="index" :style="{borderBottom: `1px solid ${border}`}">
                    <div class="info" :class="{curr: index === currentPlay}">
                      <span>{{item.songname}}</span>
                      <i style="margin: 0 6px">-</i>
                      <p class="single" v-for="(s_item, i) in item.singer" :key="s_item.id">
                        <span>{{s_item.name}}</span>
                        <span style="margin: 0 6px">{{i !== item.singer.length - 1 ? '-' : ''}}</span>
                      </p>
                    </div>
                    <div class="play-status" title="播放">
                      <Icon type="md-pause" ref="playIcon" @click="togglePlayStatus(index, 'paused')" v-if="index === currentPlay && playing && playing !== -1"/>
                      <Icon type="md-play" ref="playIcon" v-else @click="togglePlayStatus(index, 'running')"/>
                    </div>
                    <div class="dynamic" :class="{playing: index === currentPlay}">
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
              </swiper-slide>
              <div class="swiper-scrollbar" slot="scrollbar">
                <div class="swiper-scrollbar-drag" :style="{backgroundColor: border}"></div>
              </div>
            </swiper>
          </div>
        </div>
        <div class="music">
          <div class="pic-border" ref="border" :class="{begin: begin, hidden: hide}">
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
        <div class="profile-wrapper">
          <Icon type="md-skip-backward" class="comm" @click="prevMusic" />
          <Icon type="md-pause" class="comm" ref="playIcon" @click="togglePlayStatus(currentPlay, 'paused')" v-if="playing && playing !== -1"/>
          <Icon type="md-play" class="comm" ref="playIcon" v-else @click="togglePlayStatus(currentPlay, 'running')"/>
          <Icon type="md-skip-forward" class="comm" @click="nextMusic" />
        </div>
        <span class="begin-time">{{handleMusicTime(beginTime)}}</span>
        <div class="line" ref="line" @click="setTimePlay">
          <div class="current-line" ref="currentLine">
            <span ref="point" class="point" @mousedown="pointDown"></span>
          </div>
        </div>
        <span class="duration">{{handleMusicTime(endTime)}}</span>
        <div class="play-list-icon" @click="onPlayList">
          <Icon type="md-reorder"/>
        </div>

      </div>
    </div>
    <audio class="audio" ref="audio" width="0" height="0" :src="playUrl[0]" v-if="playUrl.length > 0" muted @canplay="canPlay" @ended="onEnded">
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
        currentPlay: 0,
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
        top: 0,
        lyricTimer: null,
        playing: false,
        swiperOption: {
          direction: 'vertical',
          slidesPerView: 'auto',
          freeMode: false,
          scrollbar: {
            el: '.swiper-scrollbar'
          },
          mousewheel: true
        },
        pointOpt: {
          isDown: false,
          startX: 0,
          endX: 0,
          oldWidth: 0
        },
        initPage: false
      }
    },
    computed: {
      ...mapState({
        musicOpt: state => state.music.musicOpt,
      }),
    },
    created() {
      this.rgbStyle()
    },
    mounted() {
      this.$nextTick(() => {
        this.init(false)
        window.addEventListener('storage', (e) => {
          if (e.key === 'playList' && e.newValue !== e.oldValue) {
            clearTimeout(this.lyricTimer)
            this.lyricTimer = null
            this.top = 0
            this.playList = JSON.parse(e.newValue)
            this.currentPlay = 0
            this.init(true)
            this.rgbStyle()
          }
        }, false)
      })
      window.addEventListener('beforeunload', e => this.beforeUnloadHandler(e))
      window.localStorage.setItem('isOpen', '1')
      window.localStorage.setItem('initPage', this.initPage)
    },
    methods: {
      ...mapMutations({
        updateSongUrl: 'music/updateSongUrl',
        updatePlayStatus: 'music/updatePlayStatus',
        updateMusicPic: 'music/updateMusicPic',
        updateMusicAlbumMid: 'music/updateMusicAlbumMid',
      }),
      beforeUnloadHandler (event) {
        window.localStorage.setItem('isOpen', '0')
      },
      init() {
        this.top = 0
        this.currentLyric = 0
        this.beginTime = 0
        this.rgbStyle()
        this.getAlbum()
        this.getPlayUrl()
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
          this.getLyric()
        })
      },
      togglePlayStatus(index, status) {
        this.$refs.border.style.animationPlayState = status
        if (index !== this.currentPlay) {
          this.currentPlay = index
          window.localStorage.setItem('initPage', 'true')
          this.init()
        } else {
          this.playing = !this.playing
          if (this.playing) {
            this.play()
          } else {
            this.pause()
          }
        }

      },
      currentPlayTime() {
        clearTimeout(this.lyricTimer)
        this.lyricTimer = null
        this.lyricTimer = setTimeout(() => {
          this.beginTime = parseInt(this.audio.currentTime)
          if (this.beginTime <= this.endTime) {
            this.scrollLyric()
            this.currentPlayTime()
            this.computedPrograms()
          }
        }, 1000)
      },
      scrollLyric() {
        if (this.lyricArr.length > 0) {
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
          if (this.currentPlay === this.lyricArr.length - 2) {
            const end = this.lyricArr[this.lyricArr.length - 1].time.split(':')
            if (this.beginTime >= parseInt(end[0] * 60) + parseInt(end[1])) {
              this.currentLyric = this.lyricArr.length - 1
            }
          }
        }
      },
      play() {
        this.audio.controls = true
        try {
          this.audio.play()
          this.audio.controls = false
          this.playing = true
          this.endTime = parseInt(this.audio.duration)
          this.begin = true
          this.currentPlayTime()
        } catch (e) {
        }
      },
      pause() {
        this.audio.pause()
        this.playing = false
        clearTimeout(this.lyricTimer)
        this.lyricTimer = null
      },
      prevMusic() {
        if (this.currentPlay > 0) {
          this.currentPlay -= 1
        } else {
          this.currentPlay = this.playList.length - 1
        }
        window.localStorage.setItem('initPage', 'true')
        this.init()
      },
      nextMusic() {
        window.localStorage.setItem('initPage', 'true')
        this.onEnded()
      },
      rgbStyle() {
        let r = Math.ceil(Math.random() * 255)
        let g = Math.ceil(Math.random() * 255)
        let b = Math.ceil(Math.random() * 255)
        r = r < 100 ? 100 : r
        g = g < 120 ? 140 : g
        b = b < 150 ? 166 : b
        this.border = `rgba(${r + 20}, ${g}, ${b + 30}, 0.2)`
        this.bgRgb = {
          background: `linear-gradient(to right, rgba(${r + 20}, ${g}, ${b + 40}, 1), rgba(${r + 10}, ${g - 40}, ${b + 30}, 1), rgba(${r + 30}, ${g}, ${b + 50}, 1))`
        }
      },
      onEnded() {
        if (this.currentPlay < this.playList.length - 1) {
          this.currentPlay += 1
        } else {
          this.currentPlay = 0
        }
        this.init()
      },
      canPlay(e) {
        this.audio = e.target
        setTimeout(() => {
          this.play()
        }, 500)
        /**
          if (!window.Notification) {
            console.log('不支持通知')
          } else {
            const initPage = JSON.parse(window.localStorage.getItem('initPage'))
            if (!initPage) {
              const no = new Notification('开启angle音乐播放')
              no.onclick = (e) => {
                console.log('e', e)
                Notification.requestPermission().then((result) => {
                  if (result === 'granted') {
                    this.play()
                  }
                });
              }
            } else {
              this.play()
            }
            window.localStorage.setItem('initPage', 'true')
          }
         */

      },
      onPlayList() {
        this.openList = !this.openList
      },
      handleMusicTime(time) {
        const m = Math.floor(time / 60)
        const s = time - m * 60 < 10 ? `0${time - m * 60}` : time - m * 60
        return `0${m}:${s}`
      },
      computedPrograms() {
        if (this.$refs.line) {
          const lineWidth = this.$refs.line.getBoundingClientRect().width
          const currentTime = this.audio.currentTime
          const duration = this.audio.duration
          const width = currentTime * lineWidth / duration
          this.$refs.currentLine.style.width = `${width}px`
        }

      },
      pointDown(e) {
        this.pointOpt.isDown = true
        this.pointOpt.startX = e.clientX
        this.pointOpt.oldWidth = parseInt(window.getComputedStyle(this.$refs.currentLine , null).getPropertyValue('width'))
        document.body.addEventListener('mousemove', this.pointMove, false)
        document.body.addEventListener('mouseup', (e) => {
          document.body.removeEventListener('mousemove', this.pointMove, false)
          this.pointUp(e)
        })
      },
      pointMove(e) {
        if (this.pointOpt.isDown) {
          this.pointOpt.endX = e.clientX
          const w = this.pointOpt.endX - this.pointOpt.startX
          const currW = this.pointOpt.oldWidth + w
          this.$refs.currentLine.style.width = `${currW}px`
        }
      },
      pointUp(e) {
        this.pointOpt.isDown = false
        this.pointOpt.endX = e.clientX
        const currW = parseInt(window.getComputedStyle(this.$refs.currentLine , null).getPropertyValue('width'))
        this.audio.currentTime = currW * this.audio.duration / parseInt(window.getComputedStyle(this.$refs.line , null).getPropertyValue('width'))
        this.play()
        clearTimeout(this.lyricTimer)
        this.lyricTimer = null
      },
      setTimePlay(e) {
        const w = e.offsetX
        this.$refs.currentLine.style.width = `${w}px`
        this.audio.currentTime = w * this.audio.duration / parseInt(window.getComputedStyle(this.$refs.line , null).getPropertyValue('width'))
      }
    },
    destroyed() {
      window.removeEventListener('beforeunload', e => this.beforeUnloadHandler(e))
    },
    watch: {
      currentLyric(val, old) {
        if (val !== old && val >= 7 && this.lyricArr.length - 8 >= val) {
          this.top = -(30 * (val - 7))
        } else if (val > this.lyricArr.length - 8) {
          if (val - old > 1) {
            this.top = -(30 * (val - 7))
          }
        }
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "Player";

</style>
