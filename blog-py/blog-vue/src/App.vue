<template>
  <div id="app" ref="app" :class="{mobile: isApp}">
    <div class="app-container" style="width: 100%; height: 100%" :id="isApp ? 'app-mobile' : ''">
      <mobile-nav class="app-mobile-nav" @close-menu="isOpenMenu = false" v-if="isApp" :class="{open: isOpenMenu}"></mobile-nav>
      <div class="app" style="width: 100%;" :class="{'open-menu': isOpenMenu}" v-if="$route.name !== 'Player'">
        <blog-header-top class="app-header" @open-menu="openMenu" v-if="$route.name !== 'Player'"></blog-header-top>
        <div class="app-section">
          <div class="left-container" v-if="$route.name !== 'Article' && $route.name !== 'Search' && !isApp">
            <blog-left-aside></blog-left-aside>
          </div>
          <div class="router-view">
            <router-view :key="key" ref="router" />
          </div>
          <div class="right-container" v-if="$route.name !== 'Record' && $route.name !== 'Search' && !isApp">
            <blog-home-aside></blog-home-aside>
          </div>
        </div>
      </div>
      <router-view :key="key" v-else ref="router" />
    </div>
    <transition name="mask">
      <div class="mask" v-if="isApp && isOpenMenu" @click="isOpenMenu = !isOpenMenu"></div>
    </transition>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import BlogLeftAside from './components/LeftAside/LeftAside'
  // const BlogLeftAside = () => import('./components/LeftAside/LeftAside')
  import BlogHeaderTop from './components/HeaderTop/HeaderTop'
  import BlogHomeAside from './components/RightAside/RightAside'
  import MobileNav from './components/MobileNav/MobileNav'
  export default {
    name: 'App',
    data() {
      return {
        audio: null,
        currentTime: 0,
        current_song_url: '',
        musicCanvas: null,
        isOpenMenu: false
      }
    },
    components: {
      BlogLeftAside,
      BlogHeaderTop,
      BlogHomeAside,
      MobileNav
    },
    computed: {
      key() {
        return this.$route.name !== undefined? this.$route.name + new Date(): this.$route + new Date()
      },
      ...mapState({
        isApp: state => state.common.isApp
      })
    },
    mounted() {
      if (!this.isApp) {
        document.body.classList.add('pc')
      }
    },
    methods: {
      openMenu() {
        this.isOpenMenu = !this.isOpenMenu
      }
    },
    watch: {
    }
  }
</script>

<style>
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #555;
    height: 100%;
    width: 100%;
  }
  a {
    color: #555;
  }

</style>

<style lang="less">
  .app-section {
    width: 1090px;
    margin: 0 auto;
    padding-top: .2rem;
    display: flex;
  }
  .left-container {
    width: 200px;
    //background-color: #ffffff;
    position: fixed;
    z-index: 10;

  }
  @media screen and (max-width: 1089px) {
    .left-container {
      display: none;
    }
  }
  .router-view {
    flex: 1;
    overflow: hidden;
    margin: 0 .1rem;
    min-height: 100%;
  }
  .right-container {
    flex: 0 0 270px;
    min-height: 600px;
    padding-bottom: 20px;
  }
  .mobile {
    background-color: #f3f3f3;
    overflow-x: hidden;

  }
  #app-mobile {
    margin: 0;
    .router-view {
      margin: 0;
    }
    .app-section {
      width: 100%;
      display: block;
      height: calc(100vh - 1.8rem);
      overflow-y: auto;
      -webkit-overflow-scrolling: touch
    }
    .app-mobile-nav {
      transition: all .3s;
      width: 85%;
      overflow: hidden;
      transform: translateX(-100%);
      &.open {
        transform: translateX(0);
      }
    }
  }
  .app {
    transition: all .3s;
    position: relative;
    &.open-menu {
      transform: translateX(85%);
    }
  }
  .mask {
    position: fixed;
    left: 85%;
    top: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0, 0, 0, .6);
    z-index: 12;
    &.mask-enter-active, &.mask-leave-active {
      transition: all .3s;
    }
    &.mask-enter, &.mask-leave-to {
      opacity: 0;
      left: 0;
    }
  }
</style>
