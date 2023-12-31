<template>
  <FluxLayout
    :title="Types.OUTFLUX"
    class-name="md:border-l rounded-lg md:rounded-r-lg md:rounded-l-none"
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
import { ref, watch } from 'vue';
import { TItem } from '../types/TTransaction';
import axios, { AxiosError, AxiosResponse } from 'axios';
import APIRoutes from '../enums/apiRoutes';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const modalStore = useModalStore();
const { isModalOpen, selectedModalType } = storeToRefs(modalStore);

const transactions = ref([] as TItem[]);

const fetchNegativeTransactionsFromGroup = async () => {
  if (selectedTransaction.value) {
    await axios
      .get(`${APIRoutes.FETCH_TRANSACTIONS_FROM_GROUP}${selectedTransaction.value.uuid}`)
      .then((response: AxiosResponse) => {
        const dbInfo = response.data as TItem[];
        transactions.value = dbInfo.filter((info) => {
          return info.amount < 0;
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
  await fetchNegativeTransactionsFromGroup();
}

watch(selectedTransaction, async () => {
  await fetchNegativeTransactionsFromGroup();
});

watch(isModalOpen, async (__new, __old) => {
  if (selectedModalType.value === Types.ITEM && !__new && __old) {
    await fetchNegativeTransactionsFromGroup();
  }
});
</script>
