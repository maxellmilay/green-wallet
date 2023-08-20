<template>
  <div
    class="bg-site-gray rounded-full aspect-1 w-[12rem] h-[12rem] border-[3px] border-site-primary hover:scale-110 duration-200 overflow-hidden"
  >
    <img :src="ImagePath.DEFAULT_PROFILE_PICTURE" alt="Profile Picture" />
  </div>
  <h2 class="font-karla text-3xl">{{ name }}</h2>
  <section class="flex flex-col gap-5">
    <ProfileSummaryItem :name="Summary.BALANCE" :value="balance" />
    <ProfileSummaryItem :name="Summary.EXPENSES" :value="expenses" />
    <ProfileSummaryItem :name="Summary.INCOME" :value="income" />
  </section>
</template>

<script setup lang="ts">
import ProfileSummaryItem from '../components/ProfileSummaryItem.vue';
import Summary from '../enums/summary';
import mockData from '../mockData';
import ImagePath from '../enums/imagePath';

const { balance, expenses, income } = mockData.user.data;
const { name } = mockData.user;
</script>
