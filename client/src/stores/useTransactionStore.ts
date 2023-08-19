import { defineStore } from 'pinia';
import { TTransaction, TTransactionItem } from '../types/TTransaction';
import Store from '../enums/store';

const useTransactionStore = defineStore({
  id: Store.TRANSACTION,
  state: () => ({
    selectedTransaction: {} as TTransaction,
    selectedItem: {} as TTransactionItem,
  }),
  actions: {
    setSelectedTransaction(transaction: TTransaction) {
      this.selectedTransaction = transaction;
    },
    setSelectedItem(item: TTransactionItem) {
      this.selectedItem = item;
    },
  },
});

export default useTransactionStore;
