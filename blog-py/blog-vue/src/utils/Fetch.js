require('es6-promise')
require('isomorphic-fetch')

import {
  apiHost
} from "./environment";

const Fetch = async (url, option = {}) => {
  const api = `${apiHost}${url}`;
  console.log('api, option', api, option)
  return new Promise(((resolve, reject) => {
    fetch(api, option)
      .then(response => {
        console.log(response,'------->response')
        return response.json()
      })
      .then(response => {
        resolve(response);
      })
      .catch(err => reject(err))
  }))


}

export default Fetch
