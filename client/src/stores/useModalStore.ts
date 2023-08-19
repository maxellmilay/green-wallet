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
    openItemModal(modalType: string, item: TTransactionItem) {
      if (this.isModalOpen) {
        return;
      }
      const { setSelectedItem } = useTransactionStore();
      setSelectedItem(item);
      this.selectedModalType = Types.ITEM;
      this.selectedModalFunction = modalType;
      this.isModalOpen = true;
    },
    openTransactionModal(modalType: string, transaction: TTransaction) {
      if (this.isModalOpen) {
        return;
      }
      const { setSelectedTransaction } = useTransactionStore();
      if (modalType === Types.ADD) {
        setSelectedTransaction({} as TTransaction);
      } else if (modalType === Types.UPDATE) {
        setSelectedTransaction(transaction);
      }
      this.selectedModalType = Types.TRANSACTION;
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    setSelectedModalType(type: string) {
      this.selectedModalType = type;
    },
  },
});

export default useModalStore;
