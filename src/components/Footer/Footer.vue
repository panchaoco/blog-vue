<template>
  <div class="footer">
    <div class="footer-container">
      <div class="record">
        <span>© 2015-2019</span>
        <span>备案号：粤ICP备18142919号-1</span>
      </div>
      <div class="domain">
        <router-link class="item" to="/">查看简历</router-link>
        <span class="item">联系博主</span>
        <span class="item">商业合作</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Footer"
  }
</script>

<style lang="less" scoped>
  .footer {
    padding: .3rem 0 0;
    font-size: 13px;
    .footer-container {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding-bottom: 15px;
      bottom: 0;
      flex-direction: column;
      z-index: 100;
      .record {
        span {
          margin-right: 10px;
        }
      }
      .domain {
        margin-top: 5px;
        .item {
          margin-right: 10px;
        }
      }
    }
  }
  #app-mobile {
    .footer {
      background-color: #fff;
      font-size: .26rem;
    }
  }
</style>
