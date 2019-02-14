<template>
  <div class="hot-container">
    <div class="hot-content">
      <ul>
        <li v-for="(item, index) in hots" :key="index">
          <div class="hot-item">
            <div class="content">
              <a href="javascript:;" @click="articleDetail(item)">{{item.title}}</a>
              <p>{{item.desc}}</p>
            </div>
            <img v-if="item.img" :src="item.img" alt="">
          </div>
          <div class="profile">
            <div class="item up">
              <i class="iconfont icon-praise_fill"></i>
              <span>{{item.thumbs_up_count}}</span>人点赞
            </div>
            <div class="item comment">
              <i class="iconfont icon-pinglun"></i>
              <span>{{item.comment_count}}</span>条评论
            </div>
            <div class="item share">
              <i class="iconfont icon-ziyuan1"></i>
              <span>{{item.share_count}}</span>次分享
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "HomeRecommend",
    data() {
      return {
        hots: [
        ]
      }
    },
    created() {
      this.getArticle()
    },
    methods: {
      getArticle() {
        this.$store.dispatch('article/getArticle').then(res => {
          this.hots = res.data
        })
      },
      articleDetail(item) {
        this.$router.push({
          path: '/article',
          query: {
            id: item.id
          }
        })
      }
    }
  }
</script>

<style lang="less" scoped>
 @import "./HomeRecommend";
</style>
