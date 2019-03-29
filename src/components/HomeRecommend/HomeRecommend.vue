<template>
  <div class="hot-container">
    <swiper :options="swiperOption" class="music-slider" v-if="slides.length > 0">
      <swiper-slide v-for="(slide, index) in slides" :key="index">
        <a :href="slide.link" target="_blank">
          <img :src="slide.image" alt="">
        </a>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <!--<div class="swiper-button-prev" slot="button-prev"></div>-->
      <!--<div class="swiper-button-next" slot="button-next"></div>-->
    </swiper>
    <div class="hot-content">
      <ul>
        <li v-for="(item, index) in hots" :key="item.id" @click="articleDetail(item)">
          <div class="hot-item">
            <img v-if="item.img_src" :src="item.img_src" alt="">
            <div class="content">
              <div class="top">
                <a href="javascript:;"><h1>{{item.title}}</h1></a>
                <p>{{item.desc}}</p>
              </div>
              <div class="profile">
                <div class="item up">
                  <Icon size="18" type="md-eye"/>
                  <span>{{item.look_count}}</span>人看过
                </div>
                <div class="item time">
                  <Icon type="ios-time" />&nbsp;
                  <span>{{item.update_time | formatTime}}</span>
                </div>
              </div>
            </div>

          </div>

        </li>
      </ul>
    </div>
    <!--<blog-footer></blog-footer>-->
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  export default {
    name: "HomeRecommend",
    data() {
      return {
        hots: [],
        slides: [],
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
      }
    },
    computed: {
      ...mapState({
        bodyWidth: state => state.common.bodyWidth
      })
    },
    created() {
      this.getArticle()
      this.getBanners()
    },
    methods: {
      ...mapMutations({
        updateLeftClick: 'common/updateLeftClick'
      }),
      getBanners() {
        this.$store.dispatch('common/getBanners', {
          method: 'GET',
          body: {product_name: 'article'},
        }).then(res => {
          if (res.state === 0) {
            this.slides = res.data
          }
        })
      },
      getArticle() {
        const article_type = this.$route.name !== 'Diary' ? 1 : 2
        this.$store.dispatch('article/article', {
          body: {
            article_type
          }
        }).then(res => {
          this.hots = res.data
        })
      },
      articleDetail(item) {
        const type = Number(this.$route.query.id)
        this.updateLeftClick(false)
        this.$router.push({
          path: `/diary/article/${item.id}`,
        })
      }
    },
    filters: {
      formatTime(time) {
        return time.split(/\s+/)[0]
      }
    },
    components: {
    }
  }
</script>

<style lang="less" scoped>
  @import "./HomeRecommend";
</style>
