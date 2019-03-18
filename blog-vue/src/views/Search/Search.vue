<template>
  <section class="search">
    <div class="search-content">
      <ul>
        <li v-for="(item, index) in searchData" :key="index">
          <router-link :to="`/article/${item.id}`">
            <img v-if="item.img_src" v-lazy="item.img_src" alt="">
            <img v-else v-lazy="require('../../assets/image/search/no-img.jpg')" alt="">
            <h4>{{item.title}}</h4>
            <div class="info">
              <div class="item">
                <Icon size="16" type="md-eye" />
                <span>{{item.look_count}}</span>人看过
              </div>
            </div>
          </router-link>
        </li>
      </ul>
      <div class="page-wrapper">
        <Page :total="page.total" prev-text="上一页" next-text="下一页" />
      </div>
    </div>
    <!--<blog-footer></blog-footer>-->
  </section>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogFooter from '../../components/Footer/Footer'
  export default {
    name: "Search",
    data() {
      return {
        searchData: [],
        page: {
          total: 100,
          pageSize: 15,
          page: 1
        }
      }
    },
    created() {
      this.getSearchData()
    },
    methods: {
      getSearchData() {
        const {page, pageSize} = this.page
        this.$store.dispatch('article/article', {
          body: {
            page,
            page_size: pageSize
          }
        }).then(res => {
          this.searchData = res.data
          this.page.total = res.page.total
        })
      }
    },
    components: {
      BlogHeaderTop,
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
  .search-content {
    width: 1090px;
    margin: 0 auto;
    /*background-color: #fff;*/
    ul {
      display: flex;
      margin-top: 25px;
      flex-wrap: wrap;
      padding-top: 30px;
      padding-left: 10px;
      li {
        flex: 0 0 290px;
        height: 310px;
        margin-bottom: 40px;
        margin-right: 70px;
        box-shadow: 0 0 10px rgba(44, 62, 80, 0.4);
        h4 {
          font-weight: normal;
          font-size: 12px;
          padding-left: 5px;
          color: #2c3e50;
        }
        overflow: hidden;
        img {
          width: 100%;
          height: 260px;
        }
        .info {
          display: flex;
          padding-left: 5px;
          color: #2c3e50;
          .item {
            display: flex;
            align-items: center;
            padding: 3px 0;
            span {
              margin-left: 5px;
            }
          }
        }
      }
    }
  }
  .page-wrapper {
    display: flex;
    justify-content: center;
    /deep/.ivu-page {
      .ivu-page-item-active, .ivu-page-item:hover {
        border-color: #04ee7f;
        a {
          color: #04ee7f;
        }
      }
      .ivu-page-custom-text {
        margin: 0 10px;
        padding: 0 10px;
        &:hover {
          a {
            color: #04ee7f;
          }
        }
      }
    }
  }
</style>
