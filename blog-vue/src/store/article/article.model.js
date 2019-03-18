import Axios from '../../utils/Axios'
export default {
  namespace: 'article',
  state: {
    articleList: []
  },
  mutations: {
    ['article/getArticleList'](state, article) {
      state.articleList = article
    }
  },
  actions: {
    async ['article/article']({commit, state}, payload) {
      const res = await Axios('/v1/api/article/', payload)
      return res
    },
    async ['article/category']({commit, state}, payload) {
      const res = await Axios('/v1/api/category/', payload)
      return res
    },
    async ['blog/blogInfo']({commit, state}, payload) {
      const res = await Axios('/v1/api/blog_info/', payload)
      return res
    },
    async ['article/getComment']({commit, state}, payload) {
      const res = await Axios('/v1/api/comment/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['article/addComment']({commit, state}, payload) {
      const res = await Axios('/v1/api/add_comment/', {
        method: 'POST',
        body: payload
      })
      return res
    },
  }
}
