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
    async ['article/addArticle']({commit, state}, payload) {
      const res = await Axios('/api/v1/add_article/', {
        method: 'POST',
        body: payload
      })
      return res
    },
    async ['article/updateArticle']({commit, state}, payload) {
      const res = await Axios(`/api/v1/add_article/${payload.id}/`, {
        method: 'PATCH',
        body: payload
      })
      return res
    },
    async ['article/getArticle']({commit, state}, payload) {
      const res = await Axios('/api/v1/article/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['article/getArticleDetail']({commit, state}, payload) {
      const res = await Axios('/api/v1/article_detail/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['article/getComment']({commit, state}, payload) {
      const res = await Axios('/api/v1/comment/', {
        method: 'GET',
        body: payload
      })
      return res
    },
    async ['article/addComment']({commit, state}, payload) {
      const res = await Axios('/api/v1/add_comment/', {
        method: 'POST',
        body: payload
      })
      return res
    }
  }
}
