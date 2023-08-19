<template>
  <ModalLayout @close-modal="closeModal">
    <h3 class="text-center font-karla text-lg md:text-2xl mb-4 md:mb-7">
      {{ transactionPayload.type }} Transaction
    </h3>
    <div class="flex gap-5 items-center mb-3 md:mb-5 text-[0.5rem] md:text-xs lg-text-base">
      <label for="transaction-name" class="grow font-montserrat text-right">Transaction Name</label>
      <input
        id="transaction-name"
        type="text"
        class="w-[55%] lg:w-[60%] bg-black border border-site-gray rounded px-3 py-2 md:p-4"
        v-model="transactionPayload.name"
        key="Name"
      />
    </div>
    <div class="flex justify-end text-xs gap-3">
      <button
        class="text-site-red border border-site-red hover:bg-site-green/20 px-4 py-2 rounded"
        v-if="transactionPayload.type === 'Update'"
        @click="deleteTransaction"
      >
        Delete
      </button>
      <button
        class="text-site-green border border-site-green hover:bg-site-green/20 px-4 py-2 rounded"
        @click="submitTransaction"
      >
        {{ transactionPayload.type }}
      </button>
    </div></ModalLayout
  >
</template>
<script setup lang="ts">
import { TTransactionPayload } from '../../types/TTransaction';
import ModalLayout from './ModalLayout.vue';
</script>
