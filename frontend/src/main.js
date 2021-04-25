import Vue from 'vue'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import store from '@/store'
import router from '@/router'

import axios from 'axios'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

Vue.use(BootstrapVue)

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
