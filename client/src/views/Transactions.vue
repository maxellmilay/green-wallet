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
      <div class="flex">
        <button
          class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-tl-lg hover:bg-white/10 duration-200"
          @click="openTransactionModal({ type: 'Add' } as TTransactionPayload)"
        >
          <PlusIcon class="h-6 w-6 text-white" />
        </button>
        <button
          v-for="transaction in userTransactions"
          class="py-2 px-4 text-[0.65rem] border-t-2 border-r-2 border-site-gray hover:bg-white/20 duration-200"
          :class="handleCurrentTransactionCheck(transaction) ? 'bg-white/20' : 'bg-black'"
          @click="handleTransactionClick(transaction)"
        >
          {{ transaction.name }}
        </button>
      </div>
      <div class="flex justify-end md:justify-center gap-4 h-fit">
        <button
          class="border-2 text-xs text-blue-300 border-blue-300 rounded-lg px-4 py-2 bg-black hover:bg-white/10 duration-200"
        >
          Export
        </button>
        <button
          class="border-2 text-xs text-white border-white rounded-lg px-4 py-2 bg-black hover:bg-site-red/20 hover:text-white duration-200"
          @click="openTransactionModal({ type: 'Update', name: currentTransaction.name })"
        >
          Edit
        </button>
      </div>
    </div>
    <div class="flex flex-col md:flex-row font-montserrat mb-5">
      <Influx
        @open-transaction-item-modal="(payload) => openTransactionItemModal(payload)"
        :currentTransaction="currentTransaction"
      />
      <Outflux />
    </div>
  </section>
  <TransactionItemModal
    v-if="isModalOpen && modalType === 'item'"
    @close-modal="closeModal"
    @submit-transaction-item="submitTransactionItem"
    @delete-transaction-item="deleteTransactionItem"
    :itemPayload="itemPayload"
  />
  <TransactionModal
    v-if="isModalOpen && modalType === 'transaction'"
    @close-modal="closeModal"
    @submit-transaction="submitTransaction"
    @delete-transaction="deleteTransaction"
    :transactionPayload="transactionPayload"
  />
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
import TransactionItemModal from '../components/modals/TransactionItemModal.vue';
import TransactionModal from '../components/modals/TransactionModal.vue';
import { ref, watch } from 'vue';
import mockData from '../mockData';
import { TTransaction, TItemPayload, TTransactionPayload } from '../types/TTransaction';
import { useToast } from 'vue-toast-notification';

const userTransactions = mockData.user.data.transactions;

const toast = useToast();

const isModalOpen = ref(false);
const modalType = ref('');
const currentTransaction = ref(userTransactions[0]);
const itemPayload = ref({} as TItemPayload);
const transactionPayload = ref({} as TTransactionPayload);

const openTransactionItemModal = (payload: TItemPayload) => {
  modalType.value = 'item';
  itemPayload.value = payload;
  isModalOpen.value = true;
};

const openTransactionModal = (payload: TTransactionPayload) => {
  modalType.value = 'transaction';
  transactionPayload.value = payload;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const submitTransactionItem = () => {
  toast.success('SUBMITTED!', { duration: 750 });
  isModalOpen.value = false;
};

const submitTransaction = () => {
  toast.success('SUBMITTED!', { duration: 750 });
  isModalOpen.value = false;
};

const deleteTransactionItem = () => {
  toast.error('DELETED', { duration: 750 });
  isModalOpen.value = false;
};

const deleteTransaction = () => {
  toast.error('DELETED', { duration: 750 });
  isModalOpen.value = false;
};

const handleCurrentTransactionCheck = (transaction: TTransaction) => {
  if (!transaction.name || !currentTransaction) {
    return false;
  }
  if (transaction.name === currentTransaction.value.name) {
    return true;
  } else {
    return false;
  }
};

const handleTransactionClick = (transaction: TTransaction) => {
  currentTransaction.value = transaction;
};
</script>
