<template>
  <div class="flex flex-col w-[90%] py-12 md:h-full">
    <h2 class="font-karla text-white text-4xl text-center md:text-left">Dashboard</h2>
    <div class="flex flex-col md:flex-row grow gap-10 py-10">
      <div class="flex flex-col items-center md:h-full gap-y-12">
        <SummaryItem :icon="SunIcon" :name="'Balance'" :value="3000" />
        <SummaryItem :icon="ShoppingCartIcon" :name="'Expense'" :value="2500" />
        <SummaryItem :icon="CurrencyDollarIcon" :name="'Income'" :value="5500" />
      </div>
      <div class="flex flex-col md:h-full md:grow h-[30rem] px-[10%] md:px-0">
        <h2 class="font-karla text-2xl text-center md:text-left mb-5">Transactions</h2>
        <div
          class="flex flex-col basis-0 pr-5 gap-5 grow overflow-y-scroll scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin"
        >
          <TransactionItem
            :amount="2500"
            description="Ruel Allowanceasdsadas adas dasdad sadasdas dsa dsad"
          />
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
