<template>
  <div
    class="bg-site-gray rounded-full aspect-1 w-[9rem] aspect-square border-[3px] border-site-primary hover:scale-110 duration-200 overflow-hidden"
  >
    <img :src="profileData.picture" alt="Profile Picture" class="w-full h-full" />
  </div>
  <div class="flex flex-col">
    <h2 class="font-karla text-3xl">
      {{ profileData.firstName + ' ' + profileData.lastName }}
    </h2>
    <p class="font-karla text-xs text-center">{{ profileData.email }}</p>
  </div>
  <section class="flex flex-col gap-5">
    <ProfileSummaryItem :name="Summary.BALANCE" :value="profileData.balance" />
    <ProfileSummaryItem :name="Summary.EXPENSES" :value="profileData.expenses" />
    <ProfileSummaryItem :name="Summary.INCOME" :value="profileData.income" />
  </section>
</template>

<script setup lang="ts">
import ProfileSummaryItem from '../components/ProfileSummaryItem.vue';
import Summary from '../enums/summary';
import mockData from '../mockData';
import axios, { AxiosError, AxiosResponse } from 'axios';
import { TUser } from '../types/TUser';
import { ref, Ref, inject } from 'vue';
import { VueCookies } from 'vue-cookies';

const { balance, expenses, income } = mockData.user.data;
const profileData: Ref<TUser> = ref({} as TUser);

const $cookies = inject<VueCookies>('$cookies');

const config = {
  headers: { Authorization: `Bearer ${$cookies?.get('Token')}` },
};

await axios
  .get('/social_auth/user', config)
  .then((response: AxiosResponse) => {
    const dbUserInfo = response.data;
    profileData.value = {
      firstName: dbUserInfo.first_name,
      lastName: dbUserInfo.last_name,
      email: dbUserInfo.email,
      picture: dbUserInfo.picture,
      balance: dbUserInfo.balance,
      expenses: dbUserInfo.expenses,
      income: dbUserInfo.income,
    };
  })
  .catch((error: AxiosError) => {
    console.log(error);
  });
</script>
