import { defineStore } from 'pinia';
import { TItem, TGroup } from '../types/TTransaction';
import Store from '../enums/store';
import sortTransactions from '../helper/sortTransaction';

const useTransactionStore = defineStore({
  id: Store.TRANSACTION,
  state: () => ({
    selectedTransaction: {} as TGroup,
    selectedItem: {} as TItem,
  }),
  actions: {
    setSelectedTransaction(transaction: TGroup) {
      this.selectedTransaction = transaction;
    },
    setSelectedItem(item: TItem) {
      this.selectedItem = item;
    },
  },
});

export default useTransactionStore;
