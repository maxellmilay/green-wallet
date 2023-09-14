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
    <div v-if="errors.length !== 0" class="flex flex-col items-center gap-1 mb-2 md:mb-5">
      <p class="w-fit text-red-500" v-for="error in errors">{{ error }}</p>
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
import { ref } from 'vue';
import { defaultInputString, defaultTransactionIndex } from '../../constants/defaults';
import axios, { AxiosError, AxiosResponse } from 'axios';
import useUserStore from '../../stores/useUserStore';
import Types from '../../enums/types';
import APIRoutes from '../../enums/apiRoutes';
import Errors from '../../enums/errors';
import { TGroup } from '../../types/TTransaction';
import { TUser } from '../../types/TUser';

const transactionStore = useTransactionStore();
const modalStore = useModalStore();
const userStore = useUserStore();

const { selectedTransaction } = storeToRefs(transactionStore);
const { selectedModalFunction } = storeToRefs(modalStore);
const { user } = storeToRefs(userStore);

const defaultName =
  selectedModalFunction.value === Types.ADD ? defaultInputString : selectedTransaction.value.name;

const name = ref(defaultName);
const errors = ref([] as string[]);
const groups = ref([] as TGroup[]);

const fetchTransactionGroups = async () => {
  await axios
    .get(`${APIRoutes.FETCH_TRANSACTION_GROUPS}${user.value.uuid}`)
    .then((response: AxiosResponse) => {
      const dbInfo = response.data as TGroup[];
      groups.value = dbInfo;
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

const doesGroupNameExist = async (input: string) => {
  const doesExist = (element: TGroup) => {
    return element.name === input;
  };

  await fetchTransactionGroups();

  if (groups.value.length !== 0) {
    return groups.value.some(doesExist);
  } else {
    return false;
  }
};

const handleAddGroupClick = async () => {
  if (!errors.value.includes(Errors.EMPTY_NAME)) {
    if (name.value === defaultInputString) {
      errors.value.push(Errors.EMPTY_NAME);
    }
  } else {
    if (name.value !== defaultInputString) {
      errors.value = errors.value.filter((error) => {
        return error !== Errors.EMPTY_NAME;
      });
    }
  }

  if (!errors.value.includes(Errors.NAME_ALREADY_EXISTS)) {
    if (await doesGroupNameExist(name.value)) {
      errors.value.push(Errors.NAME_ALREADY_EXISTS);
    }
  } else {
    if (!(await doesGroupNameExist(name.value))) {
      errors.value = errors.value.filter((error) => {
        return error !== Errors.NAME_ALREADY_EXISTS;
      });
    }
  }

  if (errors.value.length === 0) {
    await axios
      .post(APIRoutes.CREATE_GROUP, { name: name.value, owner: user.value.uuid })
      .then(() => {
        modalStore.closeModal(Types.ADD);
      })
      .catch((error: AxiosError) => {
        console.log(error);
      });
  }
};

const handleUpdateGroupClick = async () => {
  if (!errors.value.includes(Errors.EMPTY_NAME)) {
    if (name.value === defaultInputString) {
      errors.value.push(Errors.EMPTY_NAME);
    }
  } else {
    if (name.value !== defaultInputString) {
      errors.value = errors.value.filter((error) => {
        return error !== Errors.EMPTY_NAME;
      });
    }
  }

  if (!errors.value.includes(Errors.NAME_ALREADY_EXISTS)) {
    if (await doesGroupNameExist(name.value)) {
      errors.value.push(Errors.NAME_ALREADY_EXISTS);
    }
  } else {
    if (!(await doesGroupNameExist(name.value))) {
      errors.value = errors.value.filter((error) => {
        return error !== Errors.NAME_ALREADY_EXISTS;
      });
    }
  }

  if (errors.value.length === 0) {
    await axios
      .put(`${APIRoutes.UPDATE_GROUP}${selectedTransaction.value.uuid}`, {
        name: name.value,
        owner: user.value.uuid,
      })
      .then(() => {
        modalStore.closeModal(Types.UPDATE);
      })
      .catch((error: AxiosError) => {
        console.log(error);
      });
  }
};

const handleDeleteGroupClick = async () => {
  await axios
    .delete(`${APIRoutes.DELETE_GROUP}${selectedTransaction.value.uuid}`)
    .then(() => {
      modalStore.closeModal(Types.DELETE);
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};
</script>
