<template>
  <div
    class="flex flex-col md:w-1/2 mb-5 md:mb-0 border-site-gray border-2 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  >
    <h3 class="text-center py-7 border-b-2 border-site-gray">Influx</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <TransactionItem
        :description="transaction.name"
        :value="transaction.value"
        @open-transaction-modal="openTransactionModal"
        v-for="transaction in influx"
      />
    </div>
    <button
      class="flex justify-center items-center py-4 border-t border-site-gray rounded-bl-lg hover:bg-white/10 duration-200"
    >
      <PlusIcon class="h-6 w-6" />
    </button>
  </div>
</template>
<script setup lang="ts">
import TransactionItem from './TransactionItem.vue';
import { PlusIcon } from '@heroicons/vue/24/solid';
import mockData from '../views/mockData';
import { ref } from 'vue';

const transactionIndex = ref(0);

const { influx } = mockData.user.data.transactions[transactionIndex.value];

const emit = defineEmits(['openTransactionModal']);

const openTransactionModal = () => {
  emit('openTransactionModal');
};
</script>
