<template>
  <div
    class="flex flex-col md:w-1/2 mb-5 md:mb-0 border-site-gray border-2 md:border-r rounded-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  >
    <h3 class="text-center py-7 border-b-2 border-site-gray">Influx</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
      <TransactionItem description="Salary" :value="5500" />
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
</script>
