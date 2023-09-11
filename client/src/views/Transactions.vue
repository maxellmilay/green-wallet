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
          v-for="group in groups"
          class="py-2 px-4 text-[0.65rem] border-2 border-site-gray hover:bg-white/20 duration-200"
          :class="handleCurrentTransactionCheck(group) ? 'bg-white/20' : 'bg-black'"
          @click="transactionStore.setSelectedTransaction(group)"
        >
          {{ group.name }}
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
import { TGroup, TItem } from '../types/TTransaction';
import { defaultTransaction, defaultTransactionIndex } from '../constants/defaults';
import Types from '../enums/types';
import useTransactionStore from '../stores/useTransactionStore';
import useModalStore from '../stores/useModalStore';
import { storeToRefs } from 'pinia';
import exportFromJSON from 'export-from-json';
import { ref } from 'vue';
import axios, { AxiosResponse, AxiosError } from 'axios';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);

const transactions = ref([] as TItem[]);
const groups = ref([] as TGroup[]);

await axios
  .get('/transaction/group')
  .then((response: AxiosResponse) => {
    const dbInfo = response.data as TGroup[];
    transactionStore.setSelectedTransaction(dbInfo[defaultTransactionIndex]);
    groups.value = dbInfo;
  })
  .catch((error: AxiosError) => {
    console.log(error);
  });

await axios
  .get(`/transaction/list/${selectedTransaction.value.name}`)
  .then((response: AxiosResponse) => {
    const dbInfo = response.data as TItem[];
    transactions.value = dbInfo;
  })
  .catch((error: AxiosError) => {
    console.log(error);
  });

const modalStore = useModalStore();
const { isModalOpen, selectedModalType } = storeToRefs(modalStore);

const handleCurrentTransactionCheck = (transaction: TGroup) => {
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
  const data = selectedTransaction;
  const fileName = selectedTransaction.value.name;
  const exportType = exportFromJSON.types.csv;
  exportFromJSON({ data, fileName, exportType });
};
</script>
