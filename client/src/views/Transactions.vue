<template>
  <header
    :inert="isModalOpen"
    class="flex flex-col md:flex-row justify-between items-center w-full mb-5"
  >
    <h2 class="font-karla text-2xl md:text-4xl">Transactions</h2>
    <div class="flex flex-col items-center md:items-end">
      <p class="font-montserrat text-2xl text-site-green">{{ mockData.user.data.balance }}</p>
      <p class="font-karla font-thin text-xs md:text-base">Balance</p>
    </div>
  </header>
  <section :inert="isModalOpen" class="flex flex-col w-full">
    <div class="flex flex-col-reverse md:flex-row justify-between">
      <div class="flex flex-wrap">
        <button
          class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-tl-lg hover:bg-white/10 duration-200"
          @click="modalStore.openTransactionModal(Types.ADD, defaultTransaction)"
        >
          <PlusIcon class="h-6 w-6 text-white" />
        </button>
        <button
          v-for="transaction in userTransactions"
          class="py-2 px-4 text-[0.65rem] border-2 border-site-gray hover:bg-white/20 duration-200"
          :class="handleCurrentTransactionCheck(transaction) ? 'bg-white/20' : 'bg-black'"
          @click="transactionStore.setSelectedTransaction(transaction)"
        >
          {{ transaction.name }}
        </button>
      </div>
      <div class="flex justify-end md:justify-center gap-4 h-fit mb-4 md:mb-0">
        <button
          class="border-2 text-xs text-blue-300 border-blue-300 rounded-lg px-4 py-2 bg-black hover:bg-white/10 duration-200"
          @click="handleExportClick"
        >
          Export
        </button>
        <button
          class="border-2 text-xs text-white border-white rounded-lg px-4 py-2 bg-black hover:bg-site-red/20 hover:text-white duration-200"
          @click="modalStore.openTransactionModal(Types.UPDATE, selectedTransaction)"
        >
          Edit
        </button>
      </div>
    </div>
    <div class="flex flex-col md:flex-row font-montserrat mb-5">
      <Influx />
      <Outflux />
    </div>
  </section>
  <TransactionItemModal v-if="isModalOpen && selectedModalType === Types.ITEM" />
  <TransactionModal v-if="isModalOpen && selectedModalType === Types.TRANSACTION" />
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
import TransactionItemModal from '../components/modals/TransactionItemModal.vue';
import TransactionModal from '../components/modals/TransactionModal.vue';
import mockData from '../mockData';
import { TTransaction } from '../types/TTransaction';
import { defaultTransaction, defaultTransactionIndex } from '../constants/defaults';
import Types from '../enums/types';
import useTransactionStore from '../stores/useTransactionStore';
import useModalStore from '../stores/useModalStore';
import { storeToRefs } from 'pinia';
import exportFromJSON from 'export-from-json';
import sortTransactions from '../helper/sortTransaction';

const userTransactions = mockData.user.data.transactions;

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const modalStore = useModalStore();
const { isModalOpen, selectedModalType } = storeToRefs(modalStore);

transactionStore.setSelectedTransaction(userTransactions[defaultTransactionIndex]);

const handleCurrentTransactionCheck = (transaction: TTransaction) => {
  if (!transaction.name || !selectedTransaction) {
    return false;
  }
  if (transaction.name === selectedTransaction.value.name) {
    return true;
  } else {
    return false;
  }
};

const handleExportClick = () => {
  const data = sortTransactions(
    selectedTransaction.value.influx,
    selectedTransaction.value.outflux
  );
  const fileName = selectedTransaction.value.name;
  const exportType = exportFromJSON.types.csv;
  exportFromJSON({ data, fileName, exportType });
};
</script>
