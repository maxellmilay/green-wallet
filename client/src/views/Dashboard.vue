<template>
  <div class="flex flex-col w-[90%] py-6 md:h-full">
    <h2 class="font-karla text-white text-4xl text-center md:text-left">Dashboard</h2>
    <div class="flex flex-col md:flex-row grow gap-10 py-10">
      <section class="flex flex-col items-center md:h-full gap-y-12">
        <SummaryItem :icon="SunIcon" :name="Summary.BALANCE" :value="balance" />
        <SummaryItem :icon="ShoppingCartIcon" :name="Summary.EXPENSES" :value="expenses" />
        <SummaryItem :icon="CurrencyDollarIcon" :name="Summary.INCOME" :value="income" />
      </section>
      <section class="flex flex-col md:h-full md:grow h-[30rem] px-[10%] md:px-0">
        <div class="flex flex-col lg:flex-row justify-between mb-5 relative">
          <h3 class="font-karla text-2xl text-center md:text-left mb-2 lg:mb-0">Transactions</h3>
          <button
            class="flex justify-between items-center h-8 w-44 px-4 text-left border rounded-lg text-xs"
            @click="dropDownClick"
          >
            <p>
              {{ selectedTransaction.name }}
            </p>
            <ChevronDownIcon class="h-4 w-4" />
          </button>
          <TransactionDropdown v-if="isDropdownOpen" @close-dropdown="dropDownClick" />
        </div>
        <div
          class="flex flex-col basis-0 pr-5 gap-5 grow overflow-y-auto scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin"
        >
          <TransactionPreviewItem
            :amount="transaction.value"
            :description="transaction.name"
            v-for="transaction in sortedSelectedTransaction"
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
import useTransactionStore from '../stores/useTransactionStore';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import TransactionDropdown from '../components/TransactionDropdown.vue';
import { ChevronDownIcon } from '@heroicons/vue/24/solid';

const userData = mockData.user.data;
const { balance, expenses, income, transactions } = userData;

const isDropdownOpen = ref(false);
const transactionStore = useTransactionStore();
const { sortedSelectedTransaction, selectedTransaction } = storeToRefs(transactionStore);

transactionStore.setSelectedTransaction(transactions[defaultTransactionIndex]);

const dropDownClick = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};
</script>
