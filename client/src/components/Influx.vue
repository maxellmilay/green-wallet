<template>
  <div
    class="flex flex-col md:w-1/2 mb-5 md:mb-0 border-site-gray border-2 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  >
    <h3 class="text-center py-7 border-b-2 border-site-gray">Influx</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <TransactionItem
        :name="item.name"
        :amount="item.value"
        v-for="item in selectedTransaction.influx"
        @click="openItemModal(Types.UPDATE, item)"
      />
    </div>
    <button
      class="flex justify-center items-center py-4 border-t border-site-gray rounded-bl-lg hover:bg-white/10 duration-200"
      @click="openItemModal(Types.ADD, defaultTransactionItem)"
    >
      <PlusIcon class="h-6 w-6" />
    </button>
  </div>
</template>
<script setup lang="ts">
import TransactionItem from './TransactionItem.vue';
import { PlusIcon } from '@heroicons/vue/24/solid';
import useModalStore from '../stores/useModalStore';
import useTransactionStore from '../stores/useTransactionStore';
import { defaultTransactionItem } from '../constants/defaults';
import { storeToRefs } from 'pinia';
import { watch } from 'vue';
import Types from '../enums/types';

const transactionStore = useTransactionStore();
const { selectedTransaction, selectedItem } = storeToRefs(transactionStore);
const { openItemModal, isModalOpen } = useModalStore();

watch(selectedItem, (_new, _old) => console.log('ITEM', _new));
</script>
