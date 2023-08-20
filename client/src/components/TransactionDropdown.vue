<template>
  <div
    class="flex flex-col absolute lg:right-0 lg:top-8 lg:bottom-auto bg-black text-xs w-44 rounded-lg"
    :class="dropdownClass"
  >
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
import { computed } from 'vue';
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

const dropdownClass = computed(() => {
  return `bottom-[-${2 * transactions.length}rem]`;
});
</script>
