<template>
  <section class="left-aside">
    <ul>
      <li v-for="(item, index) in leftNav" :key="index"
          :class="{active: current === index && isLoad}"
          @click="toggle(item, index)"
      >
        <Icon :type="item.icon"></Icon>
        <span>{{item.title}}</span>
        <transition name="line">
          <strong class="line" v-show="current === index && isLoad "></strong>
        </transition>
      </li>
    </ul>
    <div class="blog-user" v-if="info">
      <a href="./img/user.jpg" download>
        <img class="user-img" width="100" height="" src="./img/user.jpg" alt="">
      </a>
      <div class="info ">
        <span class="username">代码快枪手</span>
      </div>
      <div class="cate">
        <div class="item">
          <span class="name">猿人</span>
          <span class="count">{{info.code_len}}</span>
        </div>
        <div class="item">
          <span class="name">心情</span>
          <span class="count">{{info.essay_len}}</span>
        </div>
        <div class="item">
          <span class="name">分类</span>
          <span class="count">{{info.category_len}}</span>
        </div>
      </div>
      <div class="links">
        <a href="https://github.com/pc1995" title="github" target="_blank">
          <Icon size="20" type="logo-github" />
        </a>
      </div>
    </div>
  </section>
</template>

<script>
  import {mapMutations} from 'vuex'
  import leftNav from '../../nav-route'
  export default {
    name: "LeftAside",
    data() {
      return {
        leftNav: leftNav,
        current: 0,
        route: '',
        isLoad: false,
        info: null
      }
    },
    created() {
      console.log('this.$route.path', this.$route.path)
      this.current = this.leftNav.findIndex(item => item.path === window.location.pathname)
      this.getBlogInfo()
    },
    mounted() {
      this.$nextTick(() => {
        this.isLoad = true
      })
    },
    methods: {
      ...mapMutations({
        updateLeftClick: 'common/updateLeftClick'
      }),
      toggle(item, index) {
        this.current = index
        this.updateLeftClick(true)
        setTimeout(() => {
          this.updateLeftClick(false)
        }, 600)
        this.$router.push({
          path: item.path,
          query: {
            id: index
          }
        })
      },
      getBlogInfo() {
        this.$store.dispatch('blog/blogInfo').then(res => {
          this.info = res.data
        })
      }
    },
    watch: {
      $route(val) {
        this.current = this.leftNav.findIndex(item => item.path === window.location.pathname)
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "./LeftAside";
</style>
