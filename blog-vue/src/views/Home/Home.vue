<template>
  <blog-wrapper>
    <blog-home-recommend slot="middle" />
  </blog-wrapper>
</template>

<script>
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import BlogHomeRecommend from '../../components/HomeRecommend/HomeRecommend'
  import BlogHomeAside from '../../components/RightAside/RightAside'
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogFooter from '../../components/Footer/Footer'
  export default {
    name: "Home",
    components: {
      BlogHomeRecommend,
      BlogHomeAside,
      BlogHeaderTop,
      BlogLeftAside,
      BlogWrapper,
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
  @import "./Home";
</style>
