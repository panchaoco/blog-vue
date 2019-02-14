<template>
  <section class="login-container">
    <div class="login-wrapper">
      <div class="logo">Angle Blog</div>
      <Form :model="loginForm" :label-width="60" ref="form">
        <FormItem prop="username" label="用户名">
          <Input v-model="loginForm.username" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem prop="password" label="密码">
          <Input v-model="loginForm.password" type="password" placeholder="请输入密码"></Input>
        </FormItem>
        <FormItem prop="code" label="验证码" style="margin-bottom: 10px">
          <div class="verify-code">
            <Input placeholder="请输入验证码"></Input>
            <img :src="codeImg" alt="" @click="getVerifyCode">
          </div>
        </FormItem>
        <FormItem style="margin-bottom: 10px;text-align: center">
          <div class="profile">
            <span>忘记密码?</span>
            <router-link to="/register"><span><em>注册</em></span></router-link>
          </div>
        </FormItem>
        <FormItem>
          <Button type="primary" size="large" style="width: 100%" @click="login">登录</Button>
        </FormItem>
      </Form>
    </div>
  </section>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    name: "Login",
    data() {
      return {
        loginForm: {
          username: '',
          password: '',
          code: ''
        },
        codeImg: ''
      }
    },
    created() {
      window.localStorage.clear()
      this.getVerifyCode()
    },
    methods: {
      getVerifyCode() {
        this.$store.dispatch('user/code').then(res => {
          if (res.state === 0) {
            this.codeImg = 'data:' + res.data.img
          }
        })
      },
      login() {
        this.$store.dispatch('user/login', this.loginForm).then(res => {
          if (res.token) {
            this.$router.push('/')
          }
        }).catch(err => {
          if (err && err.data) {
            Object.entries(err.data).forEach(([key, value]) => {
              value.forEach(errText => {
                this.$Message.error(`${this.filterInput(key)}: ${errText}`)
              })
            })
          }
        })
      },
      filterInput(item) {
        return item === 'username' ? '用户名' : item === 'password' ? '密码' : '验证码'
      }
    },

  }
</script>

<style lang="less" scoped>
  @import "./Login";
</style>
