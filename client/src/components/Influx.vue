<template>
  <FluxLayout
    :title="Types.INFLUX"
    class-name="mb-5 md:mb-0 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  >
    <TransactionItem
      :name="item.name"
      :amount="item.amount"
      v-for="item in transactions"
      @click="modalStore.openItemModal(Types.UPDATE, item)"
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
import { ref, watch } from 'vue';
import axios, { AxiosResponse, AxiosError } from 'axios';
import APIRoutes from '../enums/apiRoutes';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const modalStore = useModalStore();
const { isModalOpen, selectedModalType } = storeToRefs(modalStore);

const transactions = ref([] as TItem[]);

const fetchPositiveTransactionsFromGroup = async () => {
  if (selectedTransaction.value) {
    await axios
      .get(`${APIRoutes.FETCH_TRANSACTIONS_FROM_GROUP}${selectedTransaction.value.uuid}`)
      .then((response: AxiosResponse) => {
        const dbInfo = response.data as TItem[];
        transactions.value = dbInfo.filter((info) => {
          return info.amount > 0;
        });
      })
      .catch((error: AxiosError) => {
        console.log(error);
      });
  } else {
    transactions.value = [] as TItem[];
  }
};

if (selectedTransaction.value) {
  await fetchPositiveTransactionsFromGroup();
}

watch(selectedTransaction, async () => {
  await fetchPositiveTransactionsFromGroup();
});

watch(isModalOpen, async (__new, __old) => {
  if (selectedModalType.value === Types.ITEM && !__new && __old) {
    await fetchPositiveTransactionsFromGroup();
  }
});
</script>
