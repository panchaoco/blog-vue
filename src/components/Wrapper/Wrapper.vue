<template>
  <section class="main-wrapper">
    <div class="left-container" v-if="$slots.left">
      <slot name="left"></slot>
    </div>
    <transition name="main">
      <div class="main-content">
        <div class="middle-container" v-if="$slots.middle">
          <slot name="middle"></slot>
        </div>
        <div class="right-container" v-if="$slots.right">
          <slot name="right"></slot>
        </div>
      </div>
    </transition>
  </section>
</template>

<script>
  export default {
    name: "Wrapper"
  }
</script>

<style lang="less" scoped>
 @import "./Wrapper";
</style>
