import { defineStore } from 'pinia';
import Store from '../enums/store';
import { TUser } from '../types/TUser';

const useUserStore = defineStore({
  id: Store.USER,
  state: () => ({
    user: {} as TUser,
  }),
  actions: {
    setUser(u: TUser) {
      this.user = u;
    },
  },
});

export default useUserStore;
