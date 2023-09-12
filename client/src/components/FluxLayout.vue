<template>
  <div class="flex flex-col md:w-1/2 border-site-gray border-2" :class="className">
    <h3 class="text-center py-7 border-b-2 border-site-gray">{{ title }}</h3>
    <div
      class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-white/10 scrollbar-thin h-[18rem]"
    >
      <slot />
    </div>
    <button
      class="flex justify-center items-center py-4 border-t border-site-gray hover:bg-white/10 duration-200"
      @click="openItemModal(Types.ADD, defaultTransactionItem)"
      v-if="selectedTransaction"
    >
      <PlusIcon class="h-6 w-6" />
    </button>
  </div>
</template>
<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import useModalStore from '../stores/useModalStore';
import { defaultTransactionItem } from '../constants/defaults';
import Types from '../enums/types';
import useTransactionStore from '../stores/useTransactionStore';
import { storeToRefs } from 'pinia';

const { openItemModal } = useModalStore();
const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);

const { title, className } = defineProps({
  title: { type: String, required: true },
  className: { type: String, required: true },
});
</script>
