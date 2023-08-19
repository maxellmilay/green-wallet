import { defineStore } from 'pinia';
import { defaultModalType, defaultModalFunction } from '../constants/defaults';
import useTransactionStore from './useTransactionStore';
import { TTransaction, TTransactionItem } from '../types/TTransaction';
import Types from '../enums/types';
import Store from '../enums/store';

const useModalStore = defineStore({
  id: Store.MODAL,
  state: () => ({
    isModalOpen: false,
    selectedModalType: defaultModalType,
    selectedModalFunction: defaultModalFunction,
  }),
  actions: {
    openItemModal(modalFunction: string, item: TTransactionItem) {
      if (this.isModalOpen) {
        return;
      }
      const { setSelectedItem } = useTransactionStore();
      if (modalFunction === Types.UPDATE) {
        setSelectedItem(item);
      }
      this.selectedModalType = Types.ITEM;
      this.selectedModalFunction = modalFunction;
      this.isModalOpen = true;
    },
    openTransactionModal(modalFunction: string, transaction: TTransaction) {
      if (this.isModalOpen) {
        return;
      }
      const { setSelectedTransaction } = useTransactionStore();
      if (modalFunction === Types.UPDATE) {
        setSelectedTransaction(transaction);
      }
      this.selectedModalFunction = modalFunction;
      this.selectedModalType = Types.TRANSACTION;
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
      //possible data leak
    },
    setSelectedModalType(type: string) {
      this.selectedModalType = type;
    },
  },
});

export default useModalStore;
