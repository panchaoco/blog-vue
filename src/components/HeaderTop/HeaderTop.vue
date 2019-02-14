<template>
  <div class="header-container">
    <div class="header-top">
      <div class="header-wrapper">
        <div class="logo">
          <h1>
            <router-link to="/">ANGEL BLOG</router-link>
          </h1>
        </div>
        <nav class="nav-wrapper">
          <ul>
            <li v-for="(item, index) in navigation" :key="index" v-if="item.show">
              <router-link :to="item.path">{{item.name}}</router-link>
            </li>
          </ul>
          <div class="search-input">
            <Form>
              <FormItem>
                <Input placeholder="搜索内容" />
                <Icon class="md-search" type="md-search" />
              </FormItem>
            </Form>
          </div>
        </nav>
        <div class="user">
          <div class="user-info" v-if="isLogin">
            <a href="">
              <img src="./img/user.jpg" alt="">
              <span class="user-name">{{username}}</span>
            </a>
          </div>
          <div class="admin">
            <router-link to="/login"><span>{{isLogin ? '退出登录': '登录'}}</span></router-link>
            <router-link to="/register" v-if="!isLogin"><span>注册</span></router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    name: "HeaderTop",
    data() {
      return {
        navigation: [
          {name: '首页', path: '/', show: true},
          {name: '写博客', path: '/edit', show: Number(localStorage.getItem('is_super')) !== 1},
        ],
        isLogin: !!window.localStorage.getItem('token'),
        username: window.localStorage.getItem('username')
      }
    },
    created() {
      console.log('isLogin', !!window.localStorage.getItem('token'),)
    }
  }
</script>

<style lang="less" scoped>
  @import "./HeaderTop";
</style>
