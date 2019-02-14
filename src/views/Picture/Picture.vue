<template>
  <section class="picture">
    <blog-header-top />
    <blog-wrapper>
      <blog-left-aside slot="left" />
      <div class="pic-content" slot="middle">
        <ul>
          <li v-for="(item, index) in pics" :key="index" :title="item.title">
            <img :src="item.img" alt="">
            <p :title="item.desc">{{item.desc}}</p>
            <div class="count">
              <div class="item download">
                <Icon type="md-arrow-round-down" />
                <span>{{item.download_count}}</span>
              </div>
              <div class="item love">
                <Icon type="md-heart" />
                <span>{{item.download_count}}</span>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <blog-right-aside slot="right" />
    </blog-wrapper>

  </section>
</template>

<script>
  import BlogLeftAside from '../../components/LeftAside/LeftAside'
  import BlogRightAside from '../../components/RightAside/RightAside'
  import BlogWrapper from '../../components/Wrapper/Wrapper'
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  export default {
    name: "Picture",
    data() {
      return {
        pics: [
          {
            img: require('./img/20170107145148_MhsG3.jpeg'),
            title: '自由的执行',
            download_count: 200,
            startLove: 50,
            desc: '这个世界没有那么多的纯净，但依然有那么些人或者事，在浑浊的世界里独善其身，青莲不妖'
          },
          {
            img: require('./img/timg (2).jpg'),
            title: '自由的执行',
            download_count: 200,
            startLove: 50,
            desc: '这个世界没有那么多的纯净，但依然有那么些人或者事，在浑浊的世界里独善其身，青莲不妖'
          },
          {
            img: require('./img/20170107145148_MhsG3.jpeg'),
            title: '自由的执行',
            download_count: 200,
            startLove: 50,
            desc: '这个世界没有那么多的纯净，但依然有那么些人或者事，在浑浊的世界里独善其身，青莲不妖'
          },
        ]
      }
    },
    components: {
      BlogLeftAside,
      BlogRightAside,
      BlogWrapper,
      BlogHeaderTop

    }
  }
</script>

<style lang="less" scoped>
 @import "Picture";
</style>
