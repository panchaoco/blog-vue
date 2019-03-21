<template>
  <section class="music-container">
    <blog-wrapper>
      <blog-left-aside slot="left" />
      <div class="music-wrapper" slot="middle">
        <swiper :options="swiperOption" class="music-slider">
          <swiper-slide v-for="(slide, index) in slides" :key="index">
            <a :href="slide.link" target="_blank">
              <img :src="slide.image" alt="">
            </a>
          </swiper-slide>
          <div class="swiper-pagination" slot="pagination"></div>
          <!--<div class="swiper-button-prev" slot="button-prev"></div>-->
          <!--<div class="swiper-button-next" slot="button-next"></div>-->
        </swiper>
        <div class="content">
          <ul class="song-list">
            <li v-for="(item, index) in musicList" :key="index">
              <div class="song-wrapper"><dl>
                <dt @click="playMusic(item, index)">
                  <img :src="item.img_src" alt="">
                  <span class="mask">
                    <Icon type="md-play" v-if="!item.play"/>
                    <Icon type="md-pause" v-else />
                  </span>
                </dt>
                <dd>
                  <h6>
                    <span>{{item.data.songname}}</span>
                    -
                    <span class="single" v-for="(s_item, i) in item.data.singer" :key="s_item.id">
                      {{s_item.name}}
                      {{i !== item.data.singer.length - 1 ? '-' : ''}}
                    </span>
                  </h6>
                  <p>{{item.data.albumdesc}}</p>
                </dd>
              </dl>
                <div class="play-status" v-if="current === index && play">
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>

              </div>
              <!--<div class="comment">-->
                <!--<p>评论区</p>-->
                <!--<ul>-->
                  <!--<li></li>-->
                <!--</ul>-->
              <!--</div>-->
            </li>
          </ul>
          <div class="more-music">
            <span @click="moreMusic">加载更多</span>
          </div>
        </div>
      </div>
    </blog-wrapper>
    <!--<blog-footer></blog-footer>-->
  </section>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogRightAside from '../../components/RightAside/RightAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'

  import cookie from '../../utils/music/cookie'
  import getGuid from '../../utils/music/guid'
  import musicKey from '../../utils/music/music_key'
  import BlogFooter from '../../components/Footer/Footer'
  export default {
    name: "Music",
    data() {
      return {
        swiperOption: {
          slidesPerView: 1,
          spaceBetween: 30,
          // effect: 'fade',
          loop: true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          autoplay: {
            delay: 2500,
            disableOnInteraction: false
          },
        },
        slides: [],
        musicList: [
        ],
        songBegin: 0,
        songNum: 10,
        isOpen: false
      }
    },
    computed: {
      ...mapState({
        current: state => state.music.musicOpt.current,
        play: state => state.music.play,
        songList: state => state.music.songList,
      })
    },
    created() {
      this.getBanners()
      this.getMusicDate()
    },
    mounted() {
      window.addEventListener('storage', (e) => {
        if (e.key === 'isOpen') {
          const isOpen = e.newValue === '1'
          this.isOpen = isOpen
        }
      }, false)
    },
    methods: {
      ...mapMutations({
        updateSongUrl: 'music/updateSongUrl',
        updatePlayStatus: 'music/updatePlayStatus',
        updateMusicPic: 'music/updateMusicPic',
        updateMusicAlbumMid: 'music/updateMusicAlbumMid',
      }),
      getMusicDate() {
        this.$store.dispatch('music/musicDate').then(res => {
          const date = res.data[0].get_music_date
          this.getMusicList(date)
        })
      },
      getBanners() {
        this.$store.dispatch('common/getBanners', {
          method: 'GET',
          body: {product_name: 'music'},
        }).then(res => {
          if (res.state === 0) {
            this.slides = res.data
          }
        })
      },
      getMusicList(date) {
        this.$store.dispatch('music/getMusicComment', {
          date,
          g_tk: cookie.getACSRFToken(),
          song_begin: this.songBegin,
          song_num: this.songNum
        }).then(res => {
          this.musicList = res.songlist.map(item => {
            const newItem = Object.assign({}, item)
            newItem.play = false
            newItem.img_src = `//y.gtimg.cn/music/photo_new/T002R90x90M000${item.data.albummid}.jpg?max_age=${Math.ceil(Math.random() * 3000000)}`
            return newItem
          })
          this.musicList = this.musicList.filter(item => {
            return item.data.pay.payplay !== 1
          })
        })
      },
      moreMusic() {
        this.songNum += 10
        this.getMusicList()
      },
      handleCookie() {
        cookie.set("yq_index", 0, null, null, 2400)
        cookie.set("yqq_stat", 0)
      },
      playMusic(item, index) {
        const playList = window.localStorage.getItem('playList')
        let json = playList ? JSON.parse(playList) : []
        const isHave = json.filter(d => d.albumid === item.data.albumid).length === 0
        if (isHave) {
          json = [item.data].concat(json)
        }
        window.localStorage.setItem('playList', JSON.stringify(json))
        console.log('window.localStorage.getItem(\'isOpen\')', window.localStorage.getItem('isOpen'))
        if (window.localStorage.getItem('isOpen') !== '1') {
          this.isOpen = true
          window.localStorage.setItem('isOpen', '1')
          window.open('/player/' + item.data.songmid)
        }
      },
    },
    components: {
      BlogLeftAside,
      BlogWrapper,
      BlogHeaderTop,
      BlogFooter

    }
  }
</script>

<style lang="less" scoped>
  @import "./Music";
</style>
