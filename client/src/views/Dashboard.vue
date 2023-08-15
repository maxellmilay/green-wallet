<template>
  <div class="flex flex-col w-[80%] py-12 h-full">
    <h2 class="font-karla text-white text-4xl">Dashboard</h2>
    <div class="flex grow">
      <div class="flex flex-col h-full py-5 gap-y-10">
        <div class="flex items-center gap-x-2 bg-site-green rounded-xl text-black py-6 px-10">
          <SunIcon class="h-8 w-8" />
          <div class="flex flex-col gap-y-1 font-montserrat">
            <p>Net Balance</p>
            <p class="font-semibold">&#8369; 3000</p>
          </div>
        </div>
        <div class="flex items-center gap-x-2 bg-site-green rounded-xl text-black py-6 px-10">
          <SunIcon class="h-8 w-8" />
          <div class="flex flex-col gap-y-1 font-montserrat">
            <p>Net Balance</p>
            <p class="font-semibold">&#8369; 3000</p>
          </div>
        </div>
        <div class="flex items-center gap-x-2 bg-site-green rounded-xl text-black py-6 px-10">
          <SunIcon class="h-8 w-8" />
          <div class="flex flex-col gap-y-1 font-montserrat">
            <p>Net Balance</p>
            <p class="font-semibold">&#8369; 3000</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { SunIcon } from '@heroicons/vue/24/solid';
</script>
