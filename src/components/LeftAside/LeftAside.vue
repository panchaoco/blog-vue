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
  </section>
</template>

<script>
  export default {
    name: "LeftAside",
    data() {
      return {
        leftNav: [
          {
            title: '猿人',
            icon: 'md-code',
            path: '/'
          },
          {
            title: '推荐文章',
            icon: 'logo-buffer',
            path: '/'
          },
          {
            title: '听觉',
            icon: 'md-musical-notes',
            path: '/music'
          },
          {
            title: '幻想世界',
            icon: 'md-book',
            path: '/'
          },
          {
            title: '新视觉',
            icon: 'md-image',
            path: '/picture'
          }

        ],
        current: 0,
        route: '',
        isLoad: false
      }
    },
    created() {
      if (this.$route.query['id']) {
        this.current = Number(this.$route.query['id'])
      }
    },
    mounted() {
      this.$nextTick(() => {
        this.isLoad = true
      })
    },
    methods: {
      toggle(item, index) {
        this.current = index
        this.$router.push({
          path: item.path,
          query: {
            id: index
          }
        })
      }
    },
    watch: {
    }
  }
</script>

<style lang="less" scoped>
  @import "./LeftAside";
</style>
