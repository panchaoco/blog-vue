<template>
  <div id="app">
    <router-view :key="key" />
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  import BlogHeaderTop from './components/HeaderTop/HeaderTop'
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
      BlogHeaderTop,
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
    color: #2c3e50;
    height: 100%;
  }
  a {
    color: #2c3e50;
  }

</style>

<style lang="less">
  .play-animate {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    height: 3px;
    background-color: #1DC764;
    animation: playAn .8s infinite alternate;
    z-index: 12;
    .pl {
      position: relative;
      width: 100%;
      height: 3px;
      .point {
        width: 8px;
        height: 3px;
        position: absolute;
        left: 0;
        bottom: 0px;
        border-radius: 8px;
        overflow: hidden;
        background-color: #fff;
      }
    }
  }

  @keyframes playAn {
    0% {
      height: 3px;
      opacity: 1;
    }
    100% {
      height: 3px;
      opacity: 1;
    }
  }

  @keyframes point {
    0% {
      left: 0
    }
    100% {
      left: calc(100% - 32px)
    }
  }

</style>
