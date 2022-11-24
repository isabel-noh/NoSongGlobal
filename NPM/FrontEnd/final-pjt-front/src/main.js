import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

// Import Bootstrap and BootstrapVue CSS files (order is important)

// Make BootstrapVue available throughout your project
// Optionally install the BootstrapVue icon components plugin
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
