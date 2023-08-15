import Routes from '../enums/routes';
import Dashboard from '../views/Dashboard.vue';
import Login from '../views/Login.vue';
import Profile from '../views/Profile.vue';
import Transactions from '../views/Transactions.vue';

const routes = [
  { path: Routes.DEFAULT, redirect: Routes.LOGIN },
  { path: Routes.LOGIN, name: 'Login', component: Login, meta: { title: 'Login' } },
  {
    path: Routes.DASHBOARD,
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      title: 'Dashboard',
    },
  },
  {
    path: Routes.TRANSACTIONS,
    name: 'Transactions',
    component: Transactions,
    meta: {
      title: 'Transactions',
    },
  },
  {
    path: Routes.PROFILE,
    name: 'Profile',
    component: Profile,
    meta: {
      title: 'Profile',
    },
  },
];

export default routes;
