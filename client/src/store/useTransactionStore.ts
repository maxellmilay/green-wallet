import { defineStore } from 'pinia';
import { TTransaction } from '../types/TTransaction';
import { TTransactionItem } from '../types/TTransaction';

const useTransactionStore = defineStore({
  id: 'transaction',
  state: () => ({
    selectedTransaction: {} as TTransaction,
    selectedItem: {} as TTransactionItem,
  }),
});

export default useTransactionStore;
