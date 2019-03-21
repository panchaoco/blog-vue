<template>
  <div class="aside-recommend">
    <div class="hot" v-for="(item, index) in asideHot" :key="index">
      <h4>
        <Icon type="md-flame"/>
        {{item.title}}
      </h4>
      <ul>
        <li v-for="(sub_item, sub_index) in item.list"
            :key="sub_item.title"
            :style="{transition: `all 300ms ease-in-out ${sub_index * 120}ms`}"
            ref="lis">
          <p class="content">
            <span class="rank">{{sub_index + 1}}</span>
            <span>{{sub_item.title}}</span>
          </p>
        </li>
      </ul>
    </div>

    <div class="curr-time">
      <span>{{times.hours}}</span><em>:</em>
      <span>{{times.minutes}}</span><em>:</em>
      <span>{{times.seconds}}</span>
    </div>
    <div class="category">
      <div class="cate-content">
        <span v-for="item in categoryData" :key="item.id">{{item.name}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "RightAside",
    data() {
      return {
        asideHot: [
          {
            title: '热门咨询',
            list: [
              {
                title: '浏览器的渲染机制',
                className: ''
              },
              {
                title: '从零搭建Vue项目',
                className: ''
              },
              {
                title: 'Vue源码解析',
                className: ''
              },
              {
                title: 'React源码解析',
                className: ''
              },
              {
                title: '如何开发自己的webpack插件',
                className: ''
              },
              {
                title: 'scrapy爬虫',
                className: ''
              },
              {
                title: 'Django开发API',
                className: ''
              },
              {
                title: 'Django rest framework',
                className: ''
              },
              {
                title: 'Go',
                className: ''
              },
              {
                title: 'Go 框架之Beego',
                className: ''
              },
            ]
          },
        ],
        times: {
          hours: '',
          minutes: '',
          seconds: ''
        },
        timer: null,
        categoryData: []
      }
    },
    created() {
      this.getCategory()
      this.timer = window.setInterval(() => {
        this.getCurrentTime()
      }, 1000)
    },
    mounted() {
      setTimeout(() => {
        Array.from(this.$refs.lis).forEach(item => {
          item.className = 'active'
        })
      }, 20)
    },
    methods: {
      addClass(cls) {
        if (!cls) return 'active'
      },
      getCurrentTime() {
        const date = new Date()
        const h = date.getHours()
        const m = date.getMinutes()
        const s = date.getSeconds()
        this.$set(this.times, 'hours', h < 10 ? `0${h}` : h)
        this.$set(this.times, 'minutes', m < 10 ? `0${m}` : m)
        this.$set(this.times, 'seconds', s < 10 ? `0${s}` : s)
      },
      getCategory() {
        this.$store.dispatch('article/category').then(res => {
          this.categoryData = res.data
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "RightAside";
</style>
