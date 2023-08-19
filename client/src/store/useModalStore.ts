import { defineStore } from 'pinia';
import { defaultModalType } from '../constants/defaults';

const useModalStore = defineStore({
  id: 'modal',
  state: () => ({
    isModalOpen: false,
    selectedModalType: defaultModalType,
  }),
  actions: {
    openModal() {
      this.isModalOpen = true;
    },
    closModal() {
      this.isModalOpen = false;
    },
    setSelectedModalType(type: string) {
      this.selectedModalType = type;
    },
  },
});

export default useModalStore;
