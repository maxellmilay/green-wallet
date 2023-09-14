<template>
  <div
    class="flex items-center gap-x-4 hover:bg-white duration-300 rounded-xl text-black py-6 px-10 w-fit"
    :class="summaryItemColor"
  >
    <Icon class="h-8 w-8" />
    <div class="flex flex-col gap-y-1 font-montserrat">
      <p class="text-center">{{ name }}</p>
      <p class="font-semibold">&#8369; {{ value }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { FunctionalComponent, VNodeProps, HTMLAttributes, computed, markRaw } from 'vue';

import Summary from '../enums/summary';
import useTransactionStore from '../stores/useTransactionStore';
import { storeToRefs } from 'pinia';

const { icon, name, value } = defineProps({
  icon: { type: Object as () => FunctionalComponent<HTMLAttributes & VNodeProps>, required: true },
  name: { type: String, required: true },
  value: { type: Number, required: true },
});

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);

const Icon = computed(() => {
  if (icon) {
    return markRaw(icon);
  }
});

const summaryItemColor = computed(() => {
  if (name === Summary.BALANCE) {
    if (selectedTransaction.value.balance > 0) {
      return 'bg-site-green';
    } else if (selectedTransaction.value.balance < 0) {
      return 'bg-site-red';
    } else {
      return 'bg-blue-300';
    }
  } else {
    return 'bg-site-green';
  }
});
</script>
