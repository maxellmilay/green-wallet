<template>
  <FluxLayout
    :title="Types.OUTFLUX"
    class-name="md:border-l rounded-lg md:rounded-r-lg md:rounded-l-none"
  >
    <TransactionItem
      :name="item.name"
      :amount="item.value"
      v-for="item in selectedTransaction.outflux"
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
