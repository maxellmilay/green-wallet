<template>
  <div class="flex flex-col w-[90%] py-12 md:h-full">
    <h2 class="font-karla text-white text-4xl text-center md:text-left">Dashboard</h2>
    <div class="flex flex-col md:flex-row grow gap-10 py-10">
      <section class="flex flex-col items-center md:h-full gap-y-12">
        <SummaryItem :icon="SunIcon" :name="Summary.BALANCE" :value="balance" />
        <SummaryItem :icon="ShoppingCartIcon" :name="Summary.EXPENSES" :value="expenses" />
        <SummaryItem :icon="CurrencyDollarIcon" :name="Summary.INCOME" :value="income" />
      </section>
      <section class="flex flex-col md:h-full md:grow h-[30rem] px-[10%] md:px-0">
        <h3 class="font-karla text-2xl text-center md:text-left mb-5">Transactions</h3>
        <div
          class="flex flex-col basis-0 pr-5 gap-5 grow overflow-y-auto scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin"
        >
          <TransactionPreviewItem
            :amount="transaction.value"
            :description="transaction.name"
            v-for="transaction in sortedTransactions"
          />
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { SunIcon, ShoppingCartIcon, CurrencyDollarIcon } from '@heroicons/vue/24/solid';
import TransactionPreviewItem from '../components/TransactionPreviewItem.vue';
import SummaryItem from '../components/SummaryItem.vue';
import mockData from '../mockData';
import Summary from '../enums/summary';
import sortTransactions from '../helper/sortTransaction';
import { defaultTransactionIndex } from '../constants/defaults';

const userData = mockData.user.data;
const { balance, expenses, income, transactions } = userData;

const defaultTransaction = transactions[defaultTransactionIndex];

const sortedTransactions = sortTransactions(defaultTransaction.influx, defaultTransaction.outflux);
</script>
