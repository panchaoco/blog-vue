<template>
  <section class="article-container">
    <blog-header-top />
    <div class="article-content">
      <div class="render-text" >
        <div class="render" v-if="article">
          <header>
            <h4 class="art-title"><span>{{article.title}}</span></h4>
            <section class="category">
              <div class="other">
                <div class="time cate">时间：<span>{{article.create_time}}</span></div>
                <div class="type cate">所属分类：<span>web前端</span></div>
              </div>
              <div v-if="isEdit" class="update-edit" @click="updateEdit"><Icon type="ios-book-outline" /><span>继续编辑</span></div>
            </section>
          </header>
          <div class="markdown-body" v-html="article.content"></div>
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
  </section>
</template>

<script>
  import {mapState} from 'vuex'
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeAside from '../../components/RightAside/RightAside'
  import BlogComment from '../../components/Comment/Comment'
  export default {
    name: "Article",
    data() {
      return {
        article: null,
        isEdit: false,
        isThumbs: false
      }
    },
    created() {
      this.getArticleDetail()
    },
    mounted() {
      this.setHighlight()
    },
    methods: {
      getArticleDetail() {
        const id = this.$route.query.id
        this.$store.dispatch('article/getArticleDetail', {id}).then(res => {
          this.article = res.data
          if (localStorage.getItem('user_id')) {
            this.isEdit = Number(localStorage.getItem('user_id')) === res.data.user_id
          }
          this.setHighlight()
        })
      },
      setHighlight() {
        this.$nextTick(() => {
          const pres = document.querySelectorAll('pre')
          Array.from(pres).map(item => {
            item.classList.add('hljs')
          })
        })
      },
      updateEdit() {
        this.$router.push({
          path: '/edit',
          query: {
            id: this.$route.query.id
          }
        })
      },
      goThumbs(thumbs_up_count) {
        this.isThumbs = !this.isThumbs
        this.$store.dispatch('article/updateArticle', {
          thumbs_up_count: Number(thumbs_up_count) + 1,
          id: this.$route.query.id
        }).then(res => {
          this.$Message.success(res.message)
          this.getArticleDetail()
        })
        setTimeout(() => {
          this.isThumbs = !this.isThumbs
        }, 1000)
      }
    },
    components: {
      BlogHeaderTop,
      BlogHomeAside,
      BlogComment
    }
  }
</script>

<style lang="less" scoped>
  @import "./Article";
</style>
