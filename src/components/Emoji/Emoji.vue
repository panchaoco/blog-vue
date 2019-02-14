<template>
  <section class="emoji-wrapper" :class="{active: !!newVisible}" v-if="newVisible" :style="visibleStyle">
    <div class="emoji-item" @click="choiceEmoji(item)" v-for="(item, index) in icons" :key="index">
      <img :src="item.img" alt="">
    </div>
  </section>
</template>

<script>
  import emoji from '../../assets/emoji/emoji'
  export default {
    name: "Emoji",
    data() {
      return {
        icons: [],
        visibleStyle: {
          height: '0'
        },
        timer: null,
        newVisible: false
      }
    },
    props: {
      visible: {
        type: Boolean,
        default: false
      },
      height: {
        type: Number,
        default: null
      }
    },
    created() {
      this.handleEmoji()
      this.changeStyle()
    },
    methods: {
      choiceEmoji(item) {
        this.$emit('choiceEmoji', item)
      },
      changeStyle(height) {
        this.timer = setTimeout(() => {
          this.visibleStyle = {
            height: height ? height : this.newVisible ? this.height ? `${this.height}px` : '367px' : '0'
          }
          clearTimeout(this.timer)
          this.timer = null
        }, 20)
      },
      handleEmoji() {
        Object.entries(emoji).forEach(([key, val]) => {
          this.icons.push({
            name: val,
            img: require(`../../assets/emoji/emoji_res/${val}.png`),
            text: key
          })
        })
      },
    },
    watch: {
      visible(val) {
        if (val) {
          this.newVisible = val
          this.changeStyle()
        } else {
          this.changeStyle('0px')
          setTimeout(() => {
            this.newVisible = val
          }, 400)
        }

      }
    }
  }
</script>

<style lang="less" scoped>
 @import "./Emoji";
</style>
