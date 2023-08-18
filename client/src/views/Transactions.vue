<template>
  <header :inert="false" class="flex flex-col md:flex-row justify-between items-center w-full mb-5">
    <h2 class="font-karla text-2xl md:text-4xl">Transactions</h2>
    <div class="flex flex-col items-center md:items-end">
      <p class="font-montserrat text-2xl text-site-green">{{ mockData.user.data.balance }}</p>
      <p class="font-karla font-thin text-xs md:text-base">Balance</p>
    </div>
  </header>
  <section :inert="false" class="flex flex-col w-full">
    <div class="flex flex-col-reverse md:flex-row justify-between">
      <div class="flex">
        <button
          class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-tl-lg hover:bg-white/10 duration-200"
        >
          <PlusIcon class="h-6 w-6 text-white" />
        </button>
        <button
          v-for="transaction in userTransactions"
          class="py-2 px-4 text-[0.65rem] border-t-2 border-r-2 border-site-gray hover:bg-white/20 duration-200"
          :class="handleCurrentTransactionCheck(transaction) && 'bg-white/20'"
        >
          {{ transaction.name }}
        </button>
      </div>
      <div class="flex justify-end md:justify-center gap-4 h-fit">
        <button
          class="border-2 text-xs text-white border-white rounded-lg px-4 py-2 bg-black hover:bg-white/10 duration-200"
        >
          Export
        </button>
        <button
          class="border-2 text-xs text-site-red border-site-red rounded-lg px-4 py-2 bg-black hover:bg-site-red/20 hover:text-white duration-200"
        >
          Reset
        </button>
      </div>
    </div>
    <div class="flex flex-col md:flex-row font-montserrat mb-5">
      <Influx @open-transaction-item-modal="(payload) => openTransactionItemModal(payload)" />
      <Outflux />
    </div>
  </section>
  <TransactionItemModal
    v-if="isTransactionItemModalOpen"
    @close-transaction-item-modal="closeTransactionItemModal"
    @submit-transaction-item="submitTransactionItem"
    @delete-transaction-item="deleteTransactionItem"
    :payload="transactionPayload"
  />
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
import TransactionItemModal from '../components/modals/TransactionItemModal.vue';
import { onMounted, ref } from 'vue';
import mockData from '../mockData';
import { TTransaction, TTransactionPayload } from '../types/TTransaction';
import { useToast } from 'vue-toast-notification';

const toast = useToast();

const isTransactionItemModalOpen = ref(false);
const isTransactionModalOpen = ref(false);
const transactionIndex = ref(0);
const transactionPayload = ref({} as TTransactionPayload);

const userTransactions = mockData.user.data.transactions;

const openTransactionItemModal = (payload: TTransactionPayload) => {
  transactionPayload.value = payload;
  isTransactionItemModalOpen.value = true;
};

const closeTransactionItemModal = () => {
  isTransactionItemModalOpen.value = false;
};

const submitTransactionItem = () => {
  toast.success('SUBMITTED!', { duration: 750 });
  isTransactionItemModalOpen.value = false;
};

const deleteTransactionItem = () => {
  toast.error('DELETED', { duration: 750 });
  isTransactionItemModalOpen.value = false;
};

const handleCurrentTransactionCheck = (transaction: TTransaction) => {
  if (!transaction.name || !userTransactions[transactionIndex.value]) {
    return false;
  }
  if (transaction.name === userTransactions[transactionIndex.value].name) {
    return true;
  } else {
    return false;
  }
};

onMounted(() => {});
</script>
