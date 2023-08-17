<template>
  <div
    class="bg-site-gray rounded-full aspect-1 w-[12rem] h-[12rem] border-[3px] border-site-primary hover:scale-110 duration-200"
  ></div>
  <h2 class="font-karla text-3xl">Maxell Milay</h2>
  <section class="flex flex-col gap-5">
    <ProfileSummaryItem name="Balance" :value="balance" />
    <ProfileSummaryItem name="Expenses" :value="expenses" />
    <ProfileSummaryItem name="Income" :value="income" />
  </section>
</template>

<script setup lang="ts">
import ProfileSummaryItem from '../components/ProfileSummaryItem.vue';
import mockData from '../mockData';

const { balance, expenses, income } = mockData.user.data;
</script>
