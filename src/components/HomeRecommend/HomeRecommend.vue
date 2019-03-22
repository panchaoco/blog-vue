<template>
  <div class="hot-container">
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
                  <span>{{item.update_time}}</span>
                </div>
              </div>
            </div>

          </div>

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  export default {
    name: "HomeRecommend",
    data() {
      return {
        hots: [],
        slides: []
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
        console.log('this.$route', this.$route.name)
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
        console.log('type', type)
        if (type === 1) {
          this.updateLeftClick(false)
          this.$router.push({
            path: `/diary/article/${item.id}`,
            query: {
              id: -1
            }
          })
          return
        }
        this.$router.push({
          path: `/article/${item.id}`,
        })
      }
    },
  }
</script>

<style lang="less" scoped>
  @import "./HomeRecommend";
</style>
