import { defineStore } from 'pinia';
import { TTransaction, TTransactionItem } from '../types/TTransaction';
import Store from '../enums/store';
import sortTransactions from '../helper/sortTransaction';

const useTransactionStore = defineStore({
  id: Store.TRANSACTION,
  state: () => ({
    selectedTransaction: {} as TTransaction,
    selectedItem: {} as TTransactionItem,
  }),
  getters: {
    sortedSelectedTransaction: (state) =>
      sortTransactions(state.selectedTransaction.influx, state.selectedTransaction.outflux),
  },
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
