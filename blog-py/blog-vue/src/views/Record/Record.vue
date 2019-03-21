<template>
  <section class="record-container">
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
  </section>
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
        console.log('article_type', this.$route)
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
  .animateFun(@name) {
    transform: translateY(-30px);
    opacity: 0;
    animation-name: @name;
    animation-duration: .4s;
    animation-delay: .3s;
    animation-fill-mode: forwards;
    animation-timing-function: ease-in-out;
  }
  .record-container {
    margin-left: 200px;
    min-height: 100%;
  }
  .record-content {
    padding-top: 20px;
    min-height: calc(100vh - 1.8rem);
    background-color: #fff;
    padding-left: 15px;
    .record-item {
      border-left: 3px solid #eaeaea;
      font-size: 13px;
      padding-bottom: 45px;
      &:last-child {
        padding-bottom: 0;
      }
      .year {
        display: flex;
        align-items: center;
        position: relative;
        .line {
          width: 15px;
          flex: 0 0 15px;
          height: 3px;
          background-color: #eaeaea;
          margin-right: 10px;
          position: relative;
          margin-top: -15px;
          .point {
            position: absolute;
            width: 10px;
            height: 10px;
            background-color: rgba(44, 62, 80, 0.4);
            border-radius: 50%;
            left: -7.5px;
            top: -4px;
          }
        }
        .year-data {
          margin-top: -15px;
          .animateFun(year)
        }
      }
      .sub-time-wrapper {
        /*overflow: hidden;*/
      }
      li {
        height: 80px;
      }
      .sub-item {
        height: 80px;
        position: relative;
        border-bottom: 1px dotted #eaeaea;
        display: flex;
        align-items: center;
        transition: all .2s;
        .curr-time {
          margin-right: 5px;
          transition: margin-left .2s;
          display: flex;
          align-items: center;
        }
        a {
          display: block;
          flex: 1;
        }
        .title {
          margin-bottom: 5px;
        }
        .desc {
          font-size: 12px;

        }
        .line {
          width: 30px;
          flex: 0 0 30px;
          height: 2px;
          background-color: #eaeaea;
          margin-right: 8px;
          position: relative;
         .animateFun(move);
          .point {
            position: absolute;
            width: 8px;
            height: 8px;
            background-color: rgba(44, 62, 80, 0.4);
            border-radius: 50%;
            left: -6px;
            top: -3px;
            transition: all .2s;
          }
        }
        .content {
          display: flex;
          .animateFun(move);
        }
        &:hover {
          border-color: rgba(44, 62, 80, 0.59);
          .curr-time {
            margin-left: 5px;
          }
          .point {
            background-color: rgba(44, 62, 80, 0.69);
          }
        }
      }
    }
  }

  #app-mobile {
    .record-container {
      margin-left: 0;
    }
  }
  @keyframes move {
    0% {
      transform: translateY(-30px);
      opacity: 0;
    }
    100% {
      transform: translateY(0);
      opacity: 1;
    }
  }
  @keyframes year {
    0% {
      transform: translateX(-30px);
      opacity: 0;
    }
    100% {
      transform: translateX(0);
      opacity: 1;
    }
  }
</style>
