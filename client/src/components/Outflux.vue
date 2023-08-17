<template>
  <div
    class="flex flex-col md:w-1/2 border-site-gray border-2 md:border-l rounded-lg md:rounded-r-lg md:rounded-l-none"
  >
    <h3 class="text-center py-7 border-b-2 border-site-gray">Outflux</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <TransactionItem
        :description="transaction.name"
        :value="transaction.value"
        v-for="transaction in outflux"
      />
    </div>
    <button
      class="flex justify-center items-center py-4 border-t border-site-gray rounded-br-lg hover:bg-white/10 duration-200"
    >
      <PlusIcon class="h-6 w-6" />
    </button>
  </div>
</template>
<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import TransactionItem from './TransactionItem.vue';
import mockData from '../views/mockData';
import { ref } from 'vue';

const transactionIndex = ref(0);

const { outflux } = mockData.user.data.transactions[transactionIndex.value];
</script>
