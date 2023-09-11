<template>
  <FluxLayout
    :title="Types.INFLUX"
    class-name="mb-5 md:mb-0 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
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
import { TItem } from '../types/TTransaction';
import { ref } from 'vue';
import axios, { AxiosResponse, AxiosError } from 'axios';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const { openItemModal } = useModalStore();

const transactions = ref([] as TItem[]);

await axios
  .get(`/transaction/list/${selectedTransaction.value.name}`)
  .then((response: AxiosResponse) => {
    const dbInfo = response.data as TItem[];
    transactions.value = dbInfo.filter((info) => {
      return info.amount > 0;
    });
  })
  .catch((error: AxiosError) => {
    console.log(error);
  });
</script>
