<template>
  <div class="header-container">
    <div class="header-top" :class="{fixed: !isApp, music: this.$route.name === 'Music', open: isOpenMenu}">
      <div class="header-wrapper">
        <div class="logo" v-if="!isApp">
          <h1>
            <router-link to="/">ANGEL BLOG</router-link>
          </h1>
        </div>
        <nav class="nav-wrapper">
          <ul class="nav-content" v-if="isApp">
            <li class="menu" @click="openMenu">
              <Icon type="ios-menu" />
            </li>
            <li v-for="(item, index) in appNav" :key="index" v-if="$route.name === 'Home'">
              <router-link :to="item.path">{{item.name}}</router-link>
            </li>
            <li v-if="$route.name !== 'Home'">
              <router-link to="/">ANGELBLOG</router-link>
            </li>
          </ul>
          <ul v-else>
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
        appNav: [
          {name: '主页', path: '/', show: true},
          {name: '技术栈', path: '/', show: true},
          {name: '音乐馆', path: '/music', show: true},
        ],
        navigation: [
          {name: '首页', path: '/', show: true},
        ],
        isLogin: !!window.localStorage.getItem('token'),
        username: window.localStorage.getItem('username'),
        searchValue: ''
      }
    },
    props: {
      isOpenMenu: {
        type: Boolean,
        default: false
      },
      isFixed: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      ...mapState({
        isApp: state => state.common.isApp
      })
    },
    created() {
    },
    methods: {
      searchSubmit(e) {
        this.$router.push({
          path: '/search',
          query: {
            c: this.searchValue
          }
        })
      },
      openMenu() {
        this.$emit('open-menu')
      }
    },
  }
</script>

<style lang="less" scoped>
  @import "./HeaderTop";
</style>
