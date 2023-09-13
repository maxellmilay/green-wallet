<template>
  <header
    :inert="isModalOpen"
    class="flex flex-col md:flex-row justify-between items-center w-full mb-5"
  >
    <h2 class="font-karla text-2xl md:text-4xl">Transactions</h2>
    <div
      class="flex flex-col items-center md:items-end"
      v-if="groups.length !== 0 && selectedTransaction"
    >
      <p class="font-montserrat text-2xl text-site-green">{{ selectedTransaction.balance }}</p>
      <p class="font-karla font-thin text-xs md:text-base">Balance</p>
    </div>
  </header>
  <section :inert="isModalOpen" class="flex flex-col w-full">
    <div class="flex flex-col-reverse md:flex-row justify-between">
      <div class="flex flex-wrap">
        <button
          class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-tl-lg hover:bg-white/10 duration-200"
          @click="modalStore.openTransactionModal(Types.ADD)"
        >
          <PlusIcon class="h-6 w-6 text-white" />
        </button>
        <button
          v-for="group in groups"
          class="py-2 px-4 text-[0.65rem] border-2 border-site-gray hover:bg-white/20 duration-200"
          :class="
            group.name && selectedTransaction && group.name === selectedTransaction.name
              ? 'bg-white/20'
              : 'bg-black'
          "
          @click="handleGroupTabClick(group)"
        >
          {{ group.name }}
        </button>
      </div>
      <div class="flex justify-end md:justify-center gap-4 h-fit mb-4 md:mb-0">
        <button
          class="border-2 text-xs text-blue-300 border-blue-300 rounded-lg px-4 py-2 bg-black hover:bg-white/10 duration-200"
          @click="handleExportClick"
          v-if="groups.length !== 0"
        >
          Export
        </button>
        <button
          class="border-2 text-xs text-white border-white rounded-lg px-4 py-2 bg-black hover:bg-site-red/20 hover:text-white duration-200"
          @click="modalStore.openTransactionModal(Types.UPDATE)"
          v-if="groups.length !== 0"
        >
          Edit
        </button>
      </div>
    </div>
    <div class="flex flex-col md:flex-row font-montserrat mb-5">
      <Suspense>
        <template #default>
          <Influx />
        </template>
        <template #fallback>
          <FluxFallback :fluxType="Types.INFLUX" />
        </template>
      </Suspense>
      <Suspense>
        <template #default>
          <Outflux />
        </template>
        <template #fallback>
          <FluxFallback :fluxType="Types.OUTFLUX" />
        </template>
      </Suspense>
    </div>
  </section>
  <TransactionItemModal v-if="isModalOpen && selectedModalType === Types.ITEM" />
  <TransactionModal v-if="isModalOpen && selectedModalType === Types.TRANSACTION" />
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
import TransactionItemModal from '../components/modals/TransactionItemModal.vue';
import TransactionModal from '../components/modals/TransactionModal.vue';
import { TGroup, TItem } from '../types/TTransaction';
import { TUser } from '../types/TUser';
import { defaultTransactionIndex } from '../constants/defaults';
import Types from '../enums/types';
import useTransactionStore from '../stores/useTransactionStore';
import useModalStore from '../stores/useModalStore';
import { storeToRefs } from 'pinia';
import exportFromJSON from 'export-from-json';
import { ref, watch, inject } from 'vue';
import axios, { AxiosResponse, AxiosError } from 'axios';
import { VueCookies } from 'vue-cookies';
import useUserStore from '../stores/useUserStore';
import FluxFallback from '../components/fallback/FluxFallback.vue';
import APIRoutes from '../enums/apiRoutes';

const transactionStore = useTransactionStore();
const userModal = useUserStore();
const modalStore = useModalStore();

const transactions = ref([] as TItem[]);
const groups = ref([] as TGroup[]);
const profileData = ref({} as TUser);

const { user } = storeToRefs(userModal);
const { selectedTransaction } = storeToRefs(transactionStore);
const { isModalOpen, selectedModalType, selectedModalFunction } = storeToRefs(modalStore);

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
      userModal.setUser(profileData.value);
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

      if (selectedTransaction) {
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
      transactions.value = dbInfo;
    })
    .catch((error: AxiosError) => {
      console.log(error);
    });
};

if (selectedTransaction.value) {
  await fetchTransactionsFromGroup(selectedTransaction.value);
}

watch(isModalOpen, async (__new, __old) => {
  if (selectedModalType.value === Types.ITEM && !__new && __old) {
    await fetchTransactionsFromGroup(selectedTransaction.value);
  }
});

watch(isModalOpen, async (__new, __old) => {
  if (!__new && __old) {
    await fetchTransactionGroups(user.value);
  }
});

const handleExportClick = () => {
  const data = transactions.value;
  const fileName = selectedTransaction.value.name;
  const exportType = exportFromJSON.types.csv;
  if (data) {
    exportFromJSON({ data, fileName, exportType });
  }
};

const handleGroupTabClick = (group: TGroup) => {
  transactionStore.setSelectedTransaction(group);
};
</script>
