<template>
  <div class="diary-article">
    <blog-wrapper>
      <blog-left-aside slot="left"/>
      <div slot="middle" class="diary-con">
        <div class="origin" :class="{self: !!article && article.original}"><span>原创</span></div>
        <div class="render-text" :class="{show: !!article}">
          <div class="render" v-if="article">
            <header>
              <h4 class="art-title"><span>{{article.title}}</span></h4>
            </header>
            <div class="article-img">
              <img :src="article.img_src" alt="">
            </div>
            <div class="markdown-body" ref="body" v-html="article.content"></div>
          </div>
        </div>
      </div>
      <blog-home-aside slot="right" />
    </blog-wrapper>
  </div>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeAside from '../../components/RightAside/RightAside'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogFooter from '../../components/Footer/Footer'
  import mixins from '../../mixins/mixins'
  export default {
    name: "DiaryArticle",
    data() {
      return {
        article: null
      }
    },
    mixins: [mixins],
    created() {
      this.getArticleDetail()
    },
    components: {
      BlogHomeAside,
      BlogHeaderTop,
      BlogLeftAside,
      BlogWrapper,
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
  @import "./DiaryArticle";
</style>
