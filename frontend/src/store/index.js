import Vue from 'vue'
import Vuex from 'vuex'

import slots from '@/store/services/delivery-slots'
import users from '@/store/services/users'
import auth from '@/store/modules/auth'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    slots,
    users,
    auth
  }
})

export default store
