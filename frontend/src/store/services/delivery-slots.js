import axios from 'axios'

const state = {
}

const getters = {}

const mutations = {
}

const actions = {
  getDeliverySlots (context) {
    return axios.get('/api/slots/')
      .then(response => {
        console.log(response.data)
        return response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
