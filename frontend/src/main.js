import Vue from 'vue'
import App from './App.vue'
import store from './store/index.js'

import 'carbon-components/css/carbon-components.css';
import CarbonComponentsVue from '@carbon/vue/src/index';

Vue.use(CarbonComponentsVue);

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
