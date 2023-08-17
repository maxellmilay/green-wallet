<template>
  <header :inert="false" class="flex flex-col md:flex-row justify-between items-center w-full mb-5">
    <h2 class="font-karla text-2xl md:text-4xl">Transactions</h2>
    <div class="flex flex-col items-center md:items-end">
      <p class="font-montserrat text-2xl text-site-green">3000</p>
      <p class="font-karla font-thin text-xs md:text-base">Balance</p>
    </div>
  </header>
  <section :inert="false" class="flex flex-col w-full">
    <div class="flex justify-between">
      <button
        class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-t-lg hover:bg-white/10 duration-200"
      >
        <PlusIcon class="h-6 w-6 text-white" />
      </button>
      <div class="flex justify-center gap-1 h-fit">
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
      <Influx @open-transaction-modal="openTransactionModal" />
      <Outflux />
    </div>
  </section>
  <AddTransactionModal
    :isTransactionModalOpen="isTransactionModalOpen"
    @close-transaction-modal="closeTransactionModal"
  />
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
import AddTransactionModal from '../components/AddTransactionModal.vue';
import { ref } from 'vue';

const isTransactionModalOpen = ref(true);

const openTransactionModal = () => {
  isTransactionModalOpen.value = true;
};

const closeTransactionModal = () => {
  isTransactionModalOpen.value = false;
};
</script>
