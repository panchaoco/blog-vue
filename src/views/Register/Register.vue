<template>
  <section class="register-container">
    <div class="register-wrapper">
      <div class="logo">Angle Blog</div>
      <Form :model="registerForm" :label-width="80">
        <FormItem label="用户名">
          <Input v-model="registerForm.username" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="密码">
          <Input v-model="registerForm.password" type="password" placeholder="请输入密码"></Input>
        </FormItem>
        <FormItem label="确认密码">
          <Input v-model="registerForm.ok_password" type="password" placeholder="请再次输入密码"></Input>
        </FormItem>
        <FormItem label="验证码">
          <Input placeholder="请输入验证码"></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" size="large" style="width: 100%" @click="register">注册</Button>
        </FormItem>
      </Form>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Register",
    data() {
      return {
        registerForm: {
          username: '',
          password: '',
          ok_password: ''
        }
      }
    },
    methods: {
      register() {
        this.$store.dispatch('user/register', this.registerForm).then(res => {
          if (res.data.token) {
            this.$router.push('/')
          }
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "./Register";
</style>
