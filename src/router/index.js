import Vue from 'vue'
import Router from 'vue-router'
const Home = () => import('../views/Home/Home')
const Diary = () => import('../views/Diary/Diary')
const Article = () => import('../views/Article/Article')
const Music = () => import('../views/Music/Music')
const Player = () => import('../views/Player/Player')
const Search = () => import('../views/Search/Search')
const Record = () => import('../views/Record/Record')
const DiaryArticle = () => import('../views/DiaryArticle/DiaryArticle')
const BlogUser = () => import('../views/BlogUser/BlogUser')

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path:'*',redirect:{
      name: 'Home',
    }
    },
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
    },
    {
      path: '/blogUser',
      name: 'BlogUser',
      component: BlogUser
    },
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
