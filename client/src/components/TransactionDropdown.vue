<template>
  <div
    class="flex flex-col absolute lg:right-0 lg:top-8 lg:bottom-auto bg-black text-xs w-44 rounded-lg"
    :class="dropdownClass"
  >
    <button
      v-for="(transaction, index) in transactions"
      class="h-8 border-x border-b px-4 text-left hover:bg-white/30 duration-200"
      :class="borderClass(index)"
      @click="transactionClick(transaction)"
    >
      {{ transaction.name }}
    </button>
  </div>
</template>
<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import useTransactionStore from '../stores/useTransactionStore';
import { TGroup } from '../types/TTransaction';
import axios, { AxiosError, AxiosResponse } from 'axios';
import useUserStore from '../stores/useUserStore';
import { storeToRefs } from 'pinia';
import { TUser } from '../types/TUser';
import APIRoutes from '../enums/apiRoutes';

const transactions = ref([] as any);
const userModal = useUserStore();
const { user } = storeToRefs(userModal);

const fetchTransactionGroups = async (currentUser: TUser) => {
  await axios
    .get(`${APIRoutes.FETCH_TRANSACTION_GROUPS}${currentUser.uuid}`)
    .then((response: AxiosResponse) => {
      const dbInfo = response.data;
      transactions.value = dbInfo;
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

await fetchTransactionGroups(user.value);

watch(user, async (__new, __old) => {
  await fetchTransactionGroups(__new);
});

const { setSelectedTransaction } = useTransactionStore();
const emit = defineEmits(['close-dropdown']);

const borderClass = (index: number) => {
  if (index === 0) {
    return 'rounded-t-lg border-t';
  }
  if (index === transactions.length - 1) {
    return 'rounded-b-lg';
  }
};

const transactionClick = (transaction: TGroup) => {
  setSelectedTransaction(transaction);
  emit('close-dropdown');
};

const dropdownClass = computed(() => {
  return `bottom-[-${2 * transactions.length}rem]`;
});
</script>
