<template>
  <div class="flex relative flex-col w-[90%] py-6 md:h-full">
    <h2 class="font-karla text-white text-4xl text-center md:text-left">Dashboard</h2>
    <div
      class="flex flex-col md:flex-row grow gap-10 py-10"
      v-if="groups.length !== 0 && selectedTransaction"
    >
      <section class="flex flex-col items-center md:h-full gap-y-12">
        <SummaryItem :icon="SunIcon" :name="Summary.BALANCE" :value="selectedTransaction.balance" />
        <SummaryItem
          :icon="ShoppingCartIcon"
          :name="Summary.EXPENSES"
          :value="selectedTransaction.expenses"
        />
        <SummaryItem
          :icon="CurrencyDollarIcon"
          :name="Summary.INCOME"
          :value="selectedTransaction.income"
        />
      </section>
      <section class="flex flex-col md:h-full md:grow h-[30rem] px-[10%] md:px-0">
        <div class="flex flex-col lg:flex-row justify-between mb-5 relative">
          <h3 class="font-karla text-2xl text-center md:text-left mb-2 lg:mb-0">Transactions</h3>
          <button
            class="flex justify-between items-center h-8 w-44 px-4 text-left border rounded-lg text-xs"
            @click="dropDownClick"
          >
            <p>
              {{ selectedTransaction.name }}
            </p>
            <ChevronDownIcon class="h-4 w-4" />
          </button>
          <TransactionDropdown v-if="isDropdownOpen" @close-dropdown="dropDownClick" />
        </div>
        <div
          class="flex flex-col basis-0 gap-5 grow overflow-y-auto scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin"
        >
          <TransactionPreviewItem
            :amount="transaction.amount"
            :description="transaction.name"
            v-if="transactions.length !== 0"
            v-for="transaction in transactions"
          />
          <div v-else class="flex flex-col items-center gap-5 justify-center grow">
            <p class="w-fit">There are no transaction items</p>
            <button class="w-fit px-10 py-4 rounded-xl border" @click="handleAddInitialItemClick">
              Add Item
            </button>
          </div>
        </div>
      </section>
    </div>
    <div v-else class="flex flex-col justify-center items-center gap-5 grow">
      <p class="w-fit">There are no transaction groups</p>
      <button class="w-fit px-10 py-4 rounded-xl border" @click="handleAddInitialGroupClick">
        Add Group
      </button>
    </div>
    <TransactionModal v-if="isModalOpen && selectedModalType === Types.TRANSACTION" />
    <TransactionItemModal v-if="isModalOpen && selectedModalType === Types.ITEM" />
  </div>
</template>

<script setup lang="ts">
import {
  SunIcon,
  ShoppingCartIcon,
  CurrencyDollarIcon,
  ChevronDownIcon,
} from '@heroicons/vue/24/solid';
import TransactionPreviewItem from '../components/TransactionPreviewItem.vue';
import SummaryItem from '../components/SummaryItem.vue';
import Summary from '../enums/summary';
import {
  defaultTransaction,
  defaultTransactionIndex,
  defaultTransactionItem,
  defaultUser,
} from '../constants/defaults';
import useTransactionStore from '../stores/useTransactionStore';
import { storeToRefs } from 'pinia';
import { ref, inject, watch } from 'vue';
import TransactionDropdown from '../components/TransactionDropdown.vue';
import axios, { AxiosResponse, AxiosError } from 'axios';
import { TUser } from '../types/TUser';
import { VueCookies } from 'vue-cookies';
import { TGroup, TItem } from '../types/TTransaction';
import useUserStore from '../stores/useUserStore';
import TransactionModal from '../components/modals/TransactionModal.vue';
import TransactionItemModal from '../components/modals/TransactionItemModal.vue';
import useModalStore from '../stores/useModalStore';
import Types from '../enums/types';
import APIRoutes from '../enums/apiRoutes';

const transactionStore = useTransactionStore();
const userStore = useUserStore();
const modalStore = useModalStore();

const isDropdownOpen = ref(false);
const transactions = ref([] as TItem[]);
const groups = ref([] as TGroup[]);
const profileData = ref(defaultUser);

const { selectedTransaction } = storeToRefs(transactionStore);
const { user } = storeToRefs(userStore);
const { isModalOpen, selectedModalType } = storeToRefs(modalStore);

transactionStore.setSelectedTransaction(defaultTransaction);

const $cookies = inject<VueCookies>('$cookies');

const config = {
  headers: { Authorization: `Bearer ${$cookies?.get('Token')}` },
};

const fetchUserData = async () => {
  await axios
    .get(APIRoutes.FETCH_USER_DATA, config)
    .then((response: AxiosResponse) => {
      const dbUserInfo = response.data;
      profileData.value = {
        uuid: dbUserInfo.uuid,
        firstName: dbUserInfo.first_name,
        lastName: dbUserInfo.last_name,
        email: dbUserInfo.email,
        picture: dbUserInfo.picture,
        balance: dbUserInfo.balance,
        expenses: dbUserInfo.expenses,
        income: dbUserInfo.income,
        created: dbUserInfo.created,
      };
      userStore.setUser(profileData.value);
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

await fetchUserData();

const fetchTransactionGroups = async (currentUser: TUser) => {
  await axios
    .get(`${APIRoutes.FETCH_TRANSACTION_GROUPS}${currentUser.uuid}`)
    .then((response: AxiosResponse) => {
      const dbInfo = response.data as TGroup[];
      groups.value = dbInfo;
      if (selectedTransaction.value && Object.keys(selectedTransaction.value).length !== 0) {
        if (groups.value.length === 1) {
          transactionStore.setSelectedTransaction(groups.value[defaultTransactionIndex]);
        } else {
          transactionStore.setSelectedTransaction(
            groups.value.filter((group) => {
              return group.uuid === selectedTransaction.value.uuid;
            })[defaultTransactionIndex]
          );
        }
      } else {
        transactionStore.setSelectedTransaction(dbInfo[defaultTransactionIndex]);
      }
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

await fetchTransactionGroups(user.value);

const fetchTransactionsFromGroup = async (currentGroup: TGroup) => {
  await axios
    .get(`${APIRoutes.FETCH_TRANSACTIONS_FROM_GROUP}${currentGroup.uuid}`)
    .then((response: AxiosResponse) => {
      const dbInfo = response.data as TItem[];
      dbInfo.reverse();
      transactions.value = dbInfo;
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

if (selectedTransaction.value) {
  await fetchTransactionsFromGroup(selectedTransaction.value);
}

watch(user, async (__new, __old) => {
  await fetchTransactionGroups(__new);
});

watch(selectedTransaction, async (__new, __old) => {
  await fetchTransactionsFromGroup(__new);
});

watch(isModalOpen, async (__new, __old) => {
  if (!__new && __old) {
    await fetchTransactionGroups(user.value);
    await fetchTransactionsFromGroup(selectedTransaction.value);
  }
});

const dropDownClick = async () => {
  isDropdownOpen.value = !isDropdownOpen.value;
  if (isDropdownOpen && selectedTransaction.value) {
    await fetchTransactionsFromGroup(selectedTransaction.value);
  }
};

const handleAddInitialGroupClick = () => {
  modalStore.openTransactionModal(Types.ADD);
};

const handleAddInitialItemClick = () => {
  modalStore.openItemModal(Types.ADD, defaultTransactionItem);
};
</script>
