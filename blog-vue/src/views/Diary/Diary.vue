<template>
  <div>
    <blog-wrapper>
      <blog-left-aside slot="left" />
      <blog-home-recommend slot="middle" />
    </blog-wrapper>
    <!--<blog-footer></blog-footer>-->
  </div>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeRecommend from '../../components/HomeRecommend/HomeRecommend'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogFooter from '../../components/Footer/Footer'
  export default {
    name: "Diary",
    components: {
      BlogHomeRecommend,
      BlogHeaderTop,
      BlogLeftAside,
      BlogWrapper,
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
</style>
