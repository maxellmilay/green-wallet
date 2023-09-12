<template>
  <ModalLayout @close-modal="modalStore.closeModal">
    <h3 class="text-center font-karla text-lg md:text-2xl mb-4 md:mb-7">
      {{ selectedModalFunction }} Transaction
    </h3>
    <div class="flex gap-5 items-center mb-3 md:mb-5 text-[0.5rem] md:text-xs lg-text-base">
      <label for="transaction-name" class="grow font-montserrat text-right">Transaction Name</label>
      <input
        id="transaction-name"
        type="text"
        class="w-[55%] lg:w-[60%] bg-black border border-site-gray rounded px-3 py-2 md:p-4"
        v-model="name"
        key="Name"
      />
    </div>
    <div class="flex justify-end text-xs gap-3">
      <button
        class="text-site-red border border-site-red hover:bg-site-green/20 px-4 py-2 rounded"
        v-if="selectedModalFunction === 'Update'"
        @click="handleDeleteGroupClick"
      >
        Delete
      </button>
      <button
        class="text-site-green border border-site-green hover:bg-site-green/20 px-4 py-2 rounded"
        v-if="selectedModalFunction === 'Update'"
        @click="handleUpdateGroupClick"
      >
        Update
      </button>
      <button
        class="text-site-green border border-site-green hover:bg-site-green/20 px-4 py-2 rounded"
        v-if="selectedModalFunction === 'Add'"
        @click="handleAddGroupClick"
      >
        Add
      </button>
    </div></ModalLayout
  >
</template>
<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useModalStore from '../../stores/useModalStore';
import useTransactionStore from '../../stores/useTransactionStore';
import ModalLayout from './ModalLayout.vue';
import { ref, computed } from 'vue';
import { defaultInputString } from '../../constants/defaults';
import axios, { AxiosError, AxiosResponse } from 'axios';
import useUserStore from '../../stores/useUserStore';
import Types from '../../enums/types';
import { TGroup } from '../../types/TTransaction';

const transactionStore = useTransactionStore();
const { selectedTransaction } = storeToRefs(transactionStore);
const modalStore = useModalStore();
const { selectedModalFunction } = storeToRefs(modalStore);
const { user } = useUserStore();

const defaultName =
  selectedModalFunction.value === Types.ADD ? defaultInputString : selectedTransaction.value.name;

const name = ref(defaultName);

const handleAddGroupClick = async () => {
  await axios
    .post('/transaction/create-group', { name: name.value, owner: user.uuid })
    .then(() => {
      modalStore.closeModal();
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

const handleUpdateGroupClick = async () => {
  await axios
    .put(`/transaction/group/${selectedTransaction.value.uuid}`, {
      name: name.value,
      owner: user.uuid,
    })
    .then(() => {
      modalStore.closeModal();
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

const handleDeleteGroupClick = async () => {
  await axios
    .delete(`/transaction/group/${selectedTransaction.value.uuid}`)
    .then(() => {
      modalStore.closeModal();
    })
    .then(async () => {
      await axios.get(`transaction/list/group/${user.uuid}`).then((response: AxiosResponse) => {
        const dbData = response.data;
        transactionStore.setSelectedTransaction(dbData[0]);
      });
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};
</script>
