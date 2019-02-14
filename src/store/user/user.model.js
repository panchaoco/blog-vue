import Axios from '../../utils/Axios'
export default {
  namespace: 'user',
  state: {
    user: {
      token: '',
      username: '',
      user_id: null,
      isLogin: !!localStorage.getItem('token')
    }
  },
  actions: {
    async ['user/login']({commit}, payload) {
      const res = await Axios('/api/v1/login/', {
        method: 'POST',
        body: {
          username: payload.username,
          password: payload.password
        }
      })
      if (res.token) {
        localStorage.setItem('token', res.token)
        localStorage.setItem('username', res.username)
        localStorage.setItem('user_id', res.user_id)
        localStorage.setItem('is_super', res.is_super_user)
      }
      return res
    },
    async ['user/register']({commit}, payload) {
      const res = await Axios('/api/v1/register/', {
        method: 'POST',
        body: {
          username: payload.username,
          password: payload.password
        }
      })
      if (res.state === 0) {
        if (res.data.token) {
          localStorage.setItem('token', res.data.token)
          localStorage.setItem('username', res.data.username)
          localStorage.setItem('user_id', res.data.user_id)
          console.log('res.data.is_super_user', res.data.is_super_user)
          localStorage.setItem('is_super', res.data.is_super_user)
        }
      }
      return res
    },
    async ['user/code']({commit}, payload) {
      const res = await Axios('/api/v1/code/')
      console.log('res')
      return res
    }
  }
}
