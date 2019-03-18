import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home/Home'
import Diary from '../views/Diary/Diary'
import Article from '../views/Article/Article'
import Music from '../views/Music/Music'
import Player from '../views/Player/Player'
import Search from '../views/Search/Search'
import Record from '../views/Record/Record'
import DiaryArticle from '../views/DiaryArticle/DiaryArticle'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/index',
      name: 'Home',
      component: Home
    },
    {
      path: '/diary',
      name: 'Diary',
      component: Diary
    },
    {
      path: '/article/:id',
      name: 'Article',
      component: Article
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
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/record',
      name: 'Record',
      component: Record
    },
    {
      path: '/diary/article/:id',
      name: 'DiaryArticle',
      component: DiaryArticle
    }
  ]
})


// router.beforeEach((to, form, next) => {
//   Store.commit('common/updateRouter', 'start')
//   setTimeout(() => {
//     next()
//     Store.commit('common/updateRouter', 'end')
//   }, 500)
// })

export default router
