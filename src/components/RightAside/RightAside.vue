<template>
  <div class="aside-recommend">
    <div class="blog-user">
      <div class="blog-top">
        <div class="img">
          <img src="../../components/HeaderTop/img/user.jpg" alt="">
        </div>
        <section class="work">
          <div>职位：web开发工程师</div>
          <div>经验：5年</div>
        </section>
      </div>
    </div>
    <div class="hot" v-for="(item, index) in asideHot" :key="index">
      <h4><Icon type="md-flame" />{{item.title}}</h4>
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
            ]
          },
        ]
      }
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
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "RightAside";
</style>
