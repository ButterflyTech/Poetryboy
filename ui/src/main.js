import Vue from 'vue'
import App from './App.vue'

import AudioVisual from 'vue-audio-visual'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueLoading from 'vue-loading-template'

Vue.use(VueLoading, /** options **/);
Vue.use(AudioVisual);
Vue.use(VueAxios,axios);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app')
