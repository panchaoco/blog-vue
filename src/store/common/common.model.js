import Axios from '../../utils/Axios'
export default {
  namespace: 'common',
  state: {
    router: '',
    leftClick: false,
    isApp: document.documentElement.clientWidth <= 1090
  },
  mutations: {
    ['common/updateRouter'](state, router) {
      state.router = router
    },
    ['common/updateLeftClick'](state, leftClick) {
      state.leftClick = leftClick
    },
  },
  actions: {
    async ['common/getBanners']({commit}, payload) {
      const res = await Axios('/v1/api/banner/', payload)
      return res
    }
  }
}
