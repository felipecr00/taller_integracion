import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import routes from './routes';
import store from './store';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';

Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(VueMaterial);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

const router = new VueRouter({ routes });

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
