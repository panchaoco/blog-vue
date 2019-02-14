import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home/Home'
import Edit from '../views/Markdown/Markdown'
import Article from '../views/Article/Article'
import Login from '../views/Login/Login'
import Register from '../views/Register/Register'
import Picture from '../views/Picture/Picture'
import Music from '../views/Music/Music'
import Player from '../views/MusicPlay/MusicPlay'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/edit',
      name: 'Edit',
      component: Edit
    },
    {
      path: '/article',
      name: 'Article',
      component: Article
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/picture',
      name: 'Picture',
      component: Picture
    },
    {
      path: '/music',
      name: 'Music',
      component: Music
    },
    {
      path: '/player/:mid',
      name: 'Player',
      component: Player
    },
  ]
})
