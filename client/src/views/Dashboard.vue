<template>
  <div class="flex flex-col w-[90%] py-12 h-full">
    <h2 class="font-karla text-white text-4xl">Dashboard</h2>
    <div class="flex grow gap-10 py-10">
      <div class="flex flex-col h-full gap-y-12">
        <SummaryItem :icon="SunIcon" :name="'Net Balance'" :value="3000" />
        <SummaryItem :icon="ShoppingCartIcon" :name="'Expense'" :value="2500" />
        <SummaryItem :icon="CurrencyDollarIcon" :name="'Income'" :value="5500" />
      </div>
      <div class="flex flex-col h-full grow">
        <h2 class="font-karla text-2xl">Transactions</h2>
        <div
          class="flex flex-col basis-0 py-5 pr-5 gap-5 grow overflow-y-scroll scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin"
        >
          <TransactionItem :amount="2500" description="Ruel Allowanceasdsadas adas dasdad sadasdas dsa dsad" />
          <TransactionItem :amount="-2000" description="Samsung Phone Payment" />
          <TransactionItem :amount="2500" description="Ruel Allowance" />
          <TransactionItem :amount="-2000" description="Samsung Phone Payment" />
          <TransactionItem :amount="2500" description="Ruel Allowance" />
          <TransactionItem :amount="-2000" description="Samsung Phone Payment" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { SunIcon, ShoppingCartIcon, CurrencyDollarIcon } from '@heroicons/vue/24/solid';
import TransactionItem from '../components/TransactionItem.vue';
import SummaryItem from '../components/SummaryItem.vue';
</script>
