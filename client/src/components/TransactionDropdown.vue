<template>
  <div class="flex flex-col absolute lg:right-0 bottom-[-6rem] bg-black text-xs w-44 rounded-lg">
    <button
      v-for="(transaction, index) in transactions"
      class="h-8 border-x border-b px-4 text-left hover:bg-white/30 duration-200"
      :class="borderClass(index)"
      @click="transactionClick(transaction)"
    >
      {{ transaction.name }}
    </button>
  </div>
</template>
<script setup lang="ts">
import mockData from '../mockData';
import useTransactionStore from '../stores/useTransactionStore';
import { TTransaction } from '../types/TTransaction';

const { transactions } = mockData.user.data;

const { setSelectedTransaction } = useTransactionStore();
const emit = defineEmits(['close-dropdown']);

const borderClass = (index: number) => {
  if (index === 0) {
    return 'rounded-t-lg border-t';
  }
  if (index === transactions.length - 1) {
    return 'rounded-b-lg';
  }
};

const transactionClick = (transaction: TTransaction) => {
  setSelectedTransaction(transaction);
  emit('close-dropdown');
};
</script>
