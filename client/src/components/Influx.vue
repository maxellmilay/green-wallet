<template>
  <FluxLayout
    :title="Types.INFLUX"
    class-name="mb-5 md:mb-0 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  >
    <TransactionItem
      :name="item.name"
      :amount="item.value"
      v-for="item in selectedTransaction.influx"
      @click="openItemModal(Types.UPDATE, item)"
    />
  </FluxLayout>
</template>
<script setup lang="ts">
import TransactionItem from './TransactionItem.vue';
import FluxLayout from './FluxLayout.vue';
import Types from '../enums/types';
import useTransactionStore from '../stores/useTransactionStore';
import { storeToRefs } from 'pinia';
import useModalStore from '../stores/useModalStore';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const { openItemModal } = useModalStore();
</script>
