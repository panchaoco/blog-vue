<template>
  <div class="mobile-nav">
    <div class="user">
      <img width="80" src="../LeftAside/img/user.jpg" alt="">
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
  export default {
    name: "MobileNav",
    data() {
      return {
        leftNav: [
          {
            title: '猿人世界',
            icon: 'md-code',
            path: '/'
          },
          {
            title: '文人相轻',
            icon: 'logo-buffer',
            path: '/diary'
          },
          {
            title: '音乐馆',
            icon: 'md-musical-notes',
            path: '/music'
          },
          {
            title: '藏经阁',
            icon: 'md-bookmarks',
            path: '/record'
          },
          {
            title: '客户端',
            icon: 'ios-phone-portrait',
            path: '/record'
          },
        ]
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
      padding-bottom: .3rem;
      img {
        display: block;
        width: 80px;
        height: 80px;
      }
    }
    .nav {
      padding-left: .6rem;
      li {
        height: .8rem;
        line-height: .8rem;
        font-size: .3rem;
        color: #1d2134;
        display: flex;
        align-items: center;
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
