<template>
  <div class="app-wrapper">
    <section class="wrapper-section">
      <div class="main-wrapper">
        <div class="main-content" :class="{hide: routerType === 'start'}">
          <div class="middle-container" v-if="$slots.middle" :class="{animate: leftClick}">
            <slot name="middle"></slot>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import BlogFooter from '../../components/Footer/Footer'
  export default {
    name: "Wrapper",
    data() {
      return {
        hide: false
      }
    },
    computed: {
      ...mapState({
        routerType: state => state.common.router,
        leftClick: state => state.common.leftClick
      })
    },
    created() {

    },
    components: {
      BlogFooter
    }
  }
</script>

<style lang="less" scoped>
 @import "./Wrapper";
</style>
