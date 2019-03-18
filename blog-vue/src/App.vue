<template>
  <div id="app" ref="app">
    <blog-header-top v-if="$route.name !== 'Player'"></blog-header-top>
    <div class="app-section" v-if="$route.name !== 'Player'">
      <div class="left-container" v-if="$route.name !== 'Article'">
        <blog-left-aside></blog-left-aside>
      </div>
      <div class="router-view">
        <router-view :key="key" ref="router" />
      </div>
      <div class="right-container" v-if="$route.name !== 'Record'">
        <blog-home-aside></blog-home-aside>
      </div>
    </div>
    <router-view :key="key" v-else ref="router" />
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  import BlogLeftAside from './components/LeftAside/LeftAside'
  import BlogHeaderTop from './components/HeaderTop/HeaderTop'
  import BlogHomeAside from './components/RightAside/RightAside'
  export default {
    name: 'App',
    data() {
      return {
        audio: null,
        currentTime: 0,
        current_song_url: '',
        musicCanvas: null,
      }
    },
    components: {
      BlogLeftAside,
      BlogHeaderTop,
      BlogHomeAside
    },
    computed: {
      key() {
        return this.$route.name !== undefined? this.$route.name + new Date(): this.$route + new Date()
      }
    },
    mounted() {
    },
    methods: {
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
    width: calc(100%);
  }
  a {
    color: #555;
  }

</style>

<style lang="less">
  .app-section {
    width: 1090px;
    margin: 20px auto 0;
    display: flex;
  }
  .left-container {
    width: 200px;
    //background-color: #ffffff;
    filter: blur(0.4px);
    position: fixed;
    z-index: 10;

  }
  .router-view {
    flex: 1;
    margin: 0 10px;
    overflow: hidden;
  }
  .right-container {
    flex: 0 0 270px;
    min-height: 600px;
    padding-bottom: 20px;
  }

</style>
