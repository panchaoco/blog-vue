<template>
  <div class="input-comment">
    <div class="input-item">
      <Input style="width: 75%" v-model="formData.nickname" placeholder="昵称" />
      <span class="label">昵称（必填）</span>
    </div>
    <div class="input-item">
      <Input style="width: 75%" v-model="formData.email" placeholder="邮箱" />
      <span class="label">邮箱（必填）</span>
    </div>
    <div class="input-item">
      <Input type="textarea" style="width: 100%" v-model="formData.content" :rows="3" placeholder="输入评论" />
    </div>
    <div class="input-item">
      <Button type="primary" @click="submitComment">提交评论</Button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "InputComment",
    data() {
      return {
        formData: {
          nickname: '',
          email: '',
          content: ''
        }
      }
    },
    methods: {
      submitComment() {
        this.$emit('submit-comment', this.formData)
      }
    },
    watch: {
      formData: {
        handler(val) {
          this.$emit('on-change', val)
        },
        deep: true
      }
    }
  }
</script>

<style lang="less" scoped>
  .input-comment {
    border-bottom: 1px solid #ececec;
    padding-bottom: 20px;
    .input-item {
      margin-top: 15px;
      &:first-child {
        margin-top: 0;
      }
    }
    /deep/.ivu-input {
      border-radius: 0;
      border: 1px solid #eaeaea;
      &:focus {
        box-shadow: 0 0 0 #fff;
      }
    }
    .label {
      margin-left: 6px;
    }
    .profile-wrapper {
      text-align: right;
      margin-top: 20px;
      //display: flex;
      .btn {
        margin-top: 20px;
        display: flex;
        justify-content: space-between;
      }
    }
  }
</style>
