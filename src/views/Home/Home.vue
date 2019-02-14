<template>
  <div class="home">
    <blog-header-top></blog-header-top>
    <blog-wrapper>
      <blog-left-aside slot="left" />
      <blog-home-recommend slot="middle" />
      <blog-home-aside slot="right" />
    </blog-wrapper>
  </div>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeRecommend from '../../components/HomeRecommend/HomeRecommend'
  import BlogHomeAside from '../../components/RightAside/RightAside'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  export default {
    name: "Home",
    components: {
      BlogHomeRecommend,
      BlogHomeAside,
      BlogHeaderTop,
      BlogLeftAside,
      BlogWrapper
    }
  }
</script>

<style lang="less" scoped>
  @import "./Home";
</style>
