<template>
  <wrapper>
    <div class="blog-user-wrapper" slot="middle">
      <p class="item"><em></em><span>花名：<strong style="font-size: 20px; transform: scaleY(1.3)">不</strong>见其人已闻代码</span></p>
      <p class="item"><em></em><span>工作：前端开发工程师</span></p>
      <p class="item"><em></em><span>擅长：Python、JavaScript、Vue、React、Fullter、Django等</span></p>
      <p class="item desc"><Icon size="16" type="md-code" /><span>不！不^=……，不要，我……我要写到最后一刻</span></p>
      <p class="item code">
        <em></em>
        <code>
          <span>class View extends React.PureComponent {</span>
          <span style="margin-left: 20px">construct(props) {</span>
          <span style="margin-left: 40px">super(props)</span>
          <span style="margin-left: 20px">}</span>

          <span style="margin-left: 20px">render() {</span>
          <span style="margin-left: 40px">return (</span>
          <span style="margin-left: 60px">&lt;div&gt;hello word&lt;/div&gt;</span>
          <span style="margin-left: 40px">)</span>
          <span style="margin-left: 20px">}</span>
          }
        </code>
      </p>
    </div>
  </wrapper>
</template>

<script>
  import Wrapper from '../../components/Wrapper/Wrapper'
  export default {
    name: "BlogUser",
    data() {
      return {

      }
    },
    components: {
      Wrapper,
    }
  }
</script>

<style lang="less" scoped>
  .blog-user-wrapper {
    background-color: #fff;
    padding-left: 20px;
    > .item {
      min-height: 50px;
      line-height: 50px;
      position: relative;
      padding-left: 20px;
      font-size: 14px;
      color: #606063;
      > em {
        content: ' ';
        position: absolute;
        left: 0;
        top: 25px;
        margin-top: -10px;
        width: 5px;
        height: 20px;
        border-radius: 3px;
        background-color: #e8e8e8;
      }
      &.desc {
        font-weight: 600;
        padding-left: 0;
        span {
          margin-left: 10px;
        }
      }
      &.code {
        line-height: 30px;
        em {
          top: 15px;
          background-color: #2b85e4;
        }
      }
      code {

        span {
          display: block;
        }
      }
    }
  }
</style>
