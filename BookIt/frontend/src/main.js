import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import navBar from './components/navBar.vue'
import navbarUser from './components/navbarUser.vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import axios from 'axios';
import VueAxios from 'vue-axios';
const app = createApp(App);
app.use(VueAxios, axios);
app.use(router);
app.component('navBar', navBar);
app.component('navbarUser', navbarUser);
app.mount('#app');
