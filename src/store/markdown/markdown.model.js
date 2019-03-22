export default {
  namespace: 'markdown',
  state: {
    content: ''
  },
  mutations: {
    ['markdown/save'](state, renderText) {
      state.content = renderText
    }
  }
}
