<template>
  <BlogWrapper class="record-container">
    <div slot="middle">
      <ul class="record-content">
        <li class="record-item" v-for="(item, index) in dataSource" :key="index">
          <div class="year">
            <div class="line">
              <span class="point"></span>
            </div>
            <span class="year-data">{{item.year}}</span>
          </div>
          <ul class="sub-time-wrapper">
            <li v-for="sub_item in item.sub_data" :key="sub_item.id">
              <div class="sub-item">
                <div class="line">
                  <span class="point"></span>
                </div>
                <div class="content">
                  <p class="curr-time">{{sub_item.time}}</p>
                  <a href="javascript:;" @click="gotoPage(sub_item)">
                    <span class="title">{{sub_item.title}}</span>
                  </a>
                </div>
              </div>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </BlogWrapper>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  export default {
    name: "Record",
    data() {
      return {
        dataSource: []
      }
    },
    created() {
      this.getArticle()
    },
    methods: {
      getArticle() {
        this.$store.dispatch('article/article', {
          body: {
            ordering: '-update_time'
          }
        }).then(res => {
          if (res.state === 0) {
            res.data.map(item => {
              const updateTime = new Date("2018-02-15 20:30:00".replace(/-/g,'/'))
              const year = updateTime.getFullYear()
              const month = updateTime.getMonth() + 1 < 10 ? `0${updateTime.getMonth() + 1}` : updateTime.getMonth() + 1
              const date = updateTime.getDate() < 10 ? `0${updateTime.getDate()}` : updateTime.getDate()
              const have = this.dataSource.find(item => item.year === year)
              const index = this.dataSource.findIndex(item => item.year === year)
              const subItem = {
                time: `${month}-${date}`,
                id: item.id,
                title: item.title,
                desc: item.desc,
                article_type: item.article_type
              }
              if (have) {
                const data = JSON.parse(JSON.stringify(have))
                data.sub_data.push(subItem)
                this.$set(this.dataSource, index, data)
              } else {
                this.dataSource.push({
                  year,
                  sub_data: [
                    subItem
                  ]
                })
              }
            })
          }
        })
      },
      gotoPage(item) {
        const path = item.article_type === 2 ? '/diary/article' : '/article'
        this.$router.push({
          path: `${path}/${item.id}`
        })
      }
    },
    components: {
      BlogHeaderTop,
      BlogWrapper,
      BlogLeftAside
    }
  }
</script>

<style lang="less" scoped>
  @import "./Record";
</style>
