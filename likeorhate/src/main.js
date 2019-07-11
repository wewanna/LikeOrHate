import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
  watch: {
    modalOpen: function (isOpen) {
      if (isOpen) {
        document.documentElement.style.overflow = 'hidden'
        // document.documentElement is the same as using document.querySelector('#root')
      } else {
        document.documentElement.style.overflow = 'auto'
      }
    }
  }
}).$mount('#app')
