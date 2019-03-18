<template>
  <section class="article-container">
    <div class="article-content">
      <div class="render-text" :class="{show: !!article}">
        <div class="render" v-if="article">
          <header>
            <h4 class="art-title"><span>{{article.title}}</span></h4>
            <section class="category">
              <div class="other">
                <div class="time cate">时间：<span>{{article.update_time}}</span></div>
                <div class="type cate">所属分类：<span>{{article.category_type}}</span></div>
                <div class="look cate">阅读次数：<span>{{article.look_count}}</span></div>
              </div>
            </section>
          </header>
          <div class="article-img">
            <img :src="article.img_src" alt="">
          </div>
          <div class="markdown-body" ref="body" v-html="article.content"></div>
        </div>
        <div v-else class="loading-icon">
          <Spin />
        </div>
        <div class="love" v-if="article">
          <div class="love-btn" @click="goThumbs(article.thumbs_up_count)">
            <Icon class="thumbs-icon" type="md-thumbs-up" style="font-size: 16px" />
            <span class="up-text">顶一下</span>
            <em class="up-count">{{article.thumbs_up_count}} </em>
          </div>
          <span> 次</span>
          <transition name="fade">
            <div class="is-thumbs" v-if="isThumbs">
              <Icon class="thumbs-icon" type="md-thumbs-up" style="font-size: 16px" />
              <span>+1</span>
            </div>
          </transition>
        </div>
        <div class="comment">
          <blog-comment></blog-comment>
        </div>
      </div>
      <div class="aside">
        <blog-home-aside />
      </div>
    </div>
    <!--<blog-footer></blog-footer>-->
  </section>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeAside from '../../components/RightAside/RightAside'
  import BlogComment from '../../components/Comment/Comment'
  import BlogFooter from '../../components/Footer/Footer'
  import mixins from '../../mixins/mixins'
  export default {
    name: "Article",
    data() {
      return {
        article: null,
        isEdit: false,
        isThumbs: false
      }
    },
    mixins: [mixins],
    created() {
      this.getArticleDetail()
    },
    mounted() {
    },
    methods: {
    },
    components: {
      BlogHeaderTop,
      BlogHomeAside,
      BlogComment,
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
  @import "./Article";
</style>
