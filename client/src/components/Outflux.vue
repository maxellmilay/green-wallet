<template>
  <div
    class="flex flex-col md:w-1/2 border-site-gray border-2 md:border-y-2 md:border-l-2 md:border-r rounded-lg md:rounded-r-lg"
  >
    <h3 class="text-center py-7 border-b-2 border-site-gray">Outflux</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <TransactionItem description="Internet" :value="-500" />
      <TransactionItem description="Food" :value="-1000" />
      <TransactionItem description="Transportation" :value="-250" />
      <TransactionItem description="Misc" :value="-750" />
      <TransactionItem description="Internet" :value="-500" />
      <TransactionItem description="Food" :value="-1000" />
      <TransactionItem description="Transportation" :value="-250" />
      <TransactionItem description="Misc" :value="-750" />
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
</script>
