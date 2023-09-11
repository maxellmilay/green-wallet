<template>
  <FluxLayout
    :title="Types.OUTFLUX"
    class-name="md:border-l rounded-lg md:rounded-r-lg md:rounded-l-none"
  >
    <TransactionItem
      :name="item.name"
      :amount="item.amount"
      v-for="item in transactions"
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
import { ref } from 'vue';
import { TItem } from '../types/TTransaction';
import axios, { AxiosError, AxiosResponse } from 'axios';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const { openItemModal } = useModalStore();

const transactions = ref([] as TItem[]);

await axios
  .get(`/transaction/list/${selectedTransaction.value.name}`)
  .then((response: AxiosResponse) => {
    const dbInfo = response.data as TItem[];
    transactions.value = dbInfo.filter((info) => {
      return info.amount < 0;
    });
  })
  .catch((error: AxiosError) => {
    console.log(error);
  });
</script>
