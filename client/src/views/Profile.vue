<template>
  <div
    class="bg-site-gray rounded-full aspect-1 w-[12rem] h-[12rem] border-[3px] border-site-primary hover:scale-110 duration-200"
  ></div>
  <h2 class="font-karla text-3xl">Maxell Milay</h2>
  <div class="flex flex-col gap-5">
    <ProfileSummaryItem name="Balance" :value="3000" />
    <ProfileSummaryItem name="Expenses" :value="2500" />
    <ProfileSummaryItem name="Income" :value="5500" />
  </div>
</template>

<script setup lang="ts">
import ProfileSummaryItem from '../components/ProfileSummaryItem.vue';
</script>
