import { createApp } from 'vue';
import { createPinia } from 'pinia';
import VueCookies from 'vue-cookies'
import './style.css';
import App from './App.vue';
import router from './router/router';
import 'vue-toast-notification/dist/theme-sugar.css';
import axios from 'axios'

axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL;

const pinia = createPinia();
const app = createApp(App);

app.use(router);
app.use(pinia);
app.use(VueCookies);

app.mount('#app');

