import axios from 'axios'
import {
  apiHost
} from "./environment"

const instance = axios.create({
  headers: {
    Authorization: `Token ${localStorage.getItem('token')}`
  },
})

instance.interceptors.request.use(
  config => {
    return config
  }
)

instance.interceptors.response.use(
  response => {
    return response
  },
  error => {
    return error
  }
)

const Axios = async (url, options = {}) => {
  const api = url.includes('http') ? url : `${apiHost}${url}`;
  const method = (options.method || 'GET').toLocaleLowerCase()
  let res = null
  if (method === 'get') {
    const opt = {
      params: options.body
    }
    if (options.headers) {
      opt.headers = options.headers
    }
    console.log('opt', opt)
    res = await instance.get(api, opt)
  } else if (method === 'post') {
    res = await instance.post(api, options.body)
  } else if (method === 'patch') {
    res = await instance.patch(api, options.body)
  }
  return new Promise((resolve, reject) => {
    if (res && res.status >= 200 && res.status < 300) {
      return resolve(res.data)
    } else {
      return reject(res)
    }
  })
}

export default Axios
