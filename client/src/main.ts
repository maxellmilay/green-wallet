import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import { createWebHistory, createRouter } from 'vue-router';
import routes from './constants/routes';
import 'vue-toast-notification/dist/theme-sugar.css';

const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _from, next) => {
  const title = to.meta.title as string;
  if (title) {
    document.title = title;
  }
  next();
});

app.use(router);

app.mount('#app');

