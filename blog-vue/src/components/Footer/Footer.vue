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
    min-height: 150px;
    .footer-container {
      width: 100%;
      display: flex;
      align-items: center;
      height: 150px;
      /*position: fixed;*/
      justify-content: center;
      bottom: 0;
      flex-direction: column;
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
</style>
