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
      const res = await Axios('/v1/api/login/', {
        method: 'POST',
        body: {
          username: payload.username,
          password: payload.password
        }
      })
      saveUserInfo(res)
      return res
    },
    async ['user/register']({commit}, payload) {
      const res = await Axios('/v1/api/register/', {
        method: 'POST',
        body: {
          username: payload.username,
          password: payload.password
        }
      })
      saveUserInfo(res)
      return res
    },
    async ['user/code']({commit}, payload) {
      const res = await Axios('/v1/api/code/')
      console.log('res')
      return res
    }
  }
}

const saveUserInfo = (res) => {
  if (res.state === 0) {
    if (res.data.token) {
      localStorage.setItem('token', res.data.token)
      localStorage.setItem('username', res.data.username)
      localStorage.setItem('user_id', res.data.user_id)
      console.log('res.data.is_super_user', res.data.is_super_user)
      localStorage.setItem('is_super', res.data.is_super_user)
    }
  }
}
