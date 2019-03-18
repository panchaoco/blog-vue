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
            <Form @submit.native.prevent="searchSubmit">
              <FormItem>
                <Input v-model="searchValue" placeholder="搜索内容" />
                <Icon class="md-search" type="md-search" />
              </FormItem>
            </Form>
          </div>
        </nav>
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
        ],
        isLogin: !!window.localStorage.getItem('token'),
        username: window.localStorage.getItem('username'),
        searchValue: ''
      }
    },
    created() {
      console.log('isLogin', !!window.localStorage.getItem('token'),)
    },
    methods: {
      searchSubmit(e) {
        this.$router.push({
          path: '/search',
          query: {
            c: this.searchValue
          }
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "./HeaderTop";
</style>
