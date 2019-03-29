<template>
  <div class="mobile-nav">
    <div class="user">
      <img :class="{open: isOpenMenu}" width="80" src="../LeftAside/img/user.jpg" alt="">
      <h1>ANGELBLOG-码农世界</h1>
    </div>
    <ul class="nav">
      <li v-for="(item, index) in leftNav" :key="index" @click="gotoPage(item)">
        <Icon :type="item.icon" />
        <span>{{item.title}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
  import leftNav from '../../nav-route'
  export default {
    name: "MobileNav",
    data() {
      return {
        leftNav: leftNav
      }
    },
    props: {
      isOpenMenu: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      gotoPage(item) {
        this.$emit('close-menu')
        this.$router.push(item.path)
      }
    }
  }
</script>

<style lang="less" scoped>
  .mobile-nav {
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    background-color: #fff;
    padding-top: .4rem;
    .user {
      width: 100%;
      border-bottom: 1px solid #ddd;
      padding-left: .6rem;
      img {
        display: block;
        width: 80px;
        height: 80px;
        transition: transform .4s;
      }
      h1 {
        font-weight: 500;
        padding: .2rem 0;
        font-size: .30rem;
        color: #0b7eff;
      }
    }
    .nav {
      padding-left: .6rem;
      li {
        height: 1rem;
        line-height: 1rem;
        font-size: .3rem;
        color: #5f6679;
        display: flex;
        align-items: center;
        font-weight: 500;
        /deep/.ivu-icon {
          min-width: .3rem;
        }
        span {
          margin-left: .1rem;
        }
      }
    }
  }
</style>
