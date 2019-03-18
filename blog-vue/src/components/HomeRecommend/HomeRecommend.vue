<template>
  <div class="hot-container">
    <div class="hot-content">
      <ul>
        <li v-for="(item, index) in hots" :key="item.id" @click="articleDetail(item)">
          <div class="hot-item">
            <img v-if="item.img_src" :src="item.img_src" alt="">
            <div class="content">
              <div class="top">
                <a href="javascript:;"><h1>{{item.title}}</h1></a>
                <p>{{item.desc}}</p>
              </div>
              <div class="profile">
                <div class="item up">
                  <Icon size="18" type="md-eye"/>
                  <span>{{item.look_count}}</span>人看过
                </div>
                <div class="item time">
                  {{item.update_time === item.add_time ? '发布于' : '更新于'}}&nbsp;<span>{{item.update_time}}</span>
                </div>
              </div>
            </div>

          </div>

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import {mapMutations} from 'vuex'
  export default {
    name: "HomeRecommend",
    data() {
      return {
        hots: []
      }
    },
    created() {
      this.getArticle()
    },
    methods: {
      ...mapMutations({
        updateLeftClick: 'common/updateLeftClick'
      }),
      getArticle() {
        const article_type = this.$route.query.id !== undefined ? Number(this.$route.query.id) === 0 ? 1 : 2 : 1
        this.$store.dispatch('article/article', {
          body: {
            article_type
          }
        }).then(res => {
          this.hots = res.data
        })
      },
      articleDetail(item) {
        const type = Number(this.$route.query.id)
        console.log('type', type)
        if (type === 1) {
          this.updateLeftClick(false)
          this.$router.push({
            path: `/diary/article/${item.id}`,
            query: {
              id: -1
            }
          })
          return
        }
        this.$router.push({
          path: `/article/${item.id}`,
        })
      }
    },
  }
</script>

<style lang="less" scoped>
  @import "./HomeRecommend";
</style>
