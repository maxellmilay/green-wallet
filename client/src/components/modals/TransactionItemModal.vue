<template>
  <div
    v-if="isTransactionModalOpen"
    class="flex h-[100dvh] w-full justify-center items-center top-0 bg-black/80 fixed md:absolute"
    :key="payload.type.toString()"
  >
    <div class="w-[25rem] lg:w-[35rem]">
      <div class="mx-5 p-5 md:p-10 bg-black rounded-lg border">
        <div class="flex w-full justify-end">
          <button class="bg-site-red text-black rounded-full" @click="closeTransactionItemModal">
            <XMarkIcon class="h-6 w-6 p-1" />
          </button>
        </div>
        <h3 class="text-center font-karla text-lg md:text-2xl mb-4 md:mb-7">
          {{ payload.type }} Transaction
        </h3>
        <div class="flex gap-5 items-center mb-3 md:mb-5 text-[0.5rem] md:text-xs lg-text-base">
          <label for="transaction-name" class="grow font-montserrat text-right"
            >Transaction Name</label
          >
          <input
            id="transaction-name"
            type="text"
            class="w-[55%] lg:w-[60%] bg-black border border-site-gray rounded px-3 py-2 md:p-4"
            v-model="payload.description"
            key="Name"
          />
        </div>
        <div class="flex gap-5 items-center mb-5 md:mb-10 text-[0.5rem] md:text-xs lg-text-base">
          <label for="transaction-amount" class="grow font-montserrat text-right">Amount</label>
          <input
            id="transaction-amount"
            type="text"
            class="w-[55%] lg:w-[60%] bg-black border border-site-gray rounded px-3 py-2 md:p-4"
            v-model="payload.value"
            key="Amount"
          />
        </div>
        <div class="flex justify-end text-xs gap-3">
          <button
            class="text-site-red border border-site-red hover:bg-site-green/20 px-4 py-2 rounded"
            v-if="payload.type === 'Update'"
          >
            Delete
          </button>
          <button
            class="text-site-green border border-site-green hover:bg-site-green/20 px-4 py-2 rounded"
          >
            {{ payload.type }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { XMarkIcon } from '@heroicons/vue/24/solid';
import { TTransactionPayload } from '../../types/TTransaction';

const { isTransactionModalOpen, payload } = defineProps({
  isTransactionModalOpen: Boolean,
  payload: { type: Object as () => TTransactionPayload, required: true },
});

const emit = defineEmits(['closeTransactionItemModal']);

const closeTransactionItemModal = () => {
  emit('closeTransactionItemModal');
};
</script>
