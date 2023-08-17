<template>
  <div class="flex flex-col w-1/2 border-site-gray border-y-2 border-l-2 border-r rounded-r-lg">
    <h3 class="text-center py-7 border-b-2 border-site-gray">Influx</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin h-[18rem]"
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
