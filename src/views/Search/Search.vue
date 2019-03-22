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
    </div>
    <!--<blog-footer></blog-footer>-->
  </section>
</template>

<script>
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
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
  .search-content {
    width: 100%;
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
        margin-right: 60px;
        box-shadow: 0 0 10px rgba(44, 62, 80, 0.4);
        h4 {
          font-weight: normal;
          font-size: 12px;
          padding-left: 5px;
          color: #2c3e50;
          background-color: #fff;
          padding-top: .1rem;
        }
        overflow: hidden;
        img {
          width: 100%;
          height: 260px;
          display: block;
        }
        .info {
          display: flex;
          padding-left: 5px;
          background-color: #fff;
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
  #app-mobile {
    .search-content {
      ul {
        flex-direction: inherit;
        justify-content: space-between;
        margin-top: 0;
        padding: 0 .1rem;
        li {
          flex: 0 0 49.4%;
          margin: 0;
          height: auto;
          margin-bottom: .1rem;
          box-shadow: none;
          border: 1px solid #eaeaea;
          img {
            height: 2rem;
          }
        }
      }
    }
  }
</style>
