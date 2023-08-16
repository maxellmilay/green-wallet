<template>
  <header class="flex justify-between items-center w-full mb-5">
    <h2 class="font-karla text-4xl">Transactions</h2>
    <div class="flex flex-col items-end">
      <p class="font-montserrat text-2xl text-site-green">16300</p>
      <p class="font-karla font-thin">Balance</p>
    </div>
  </header>
  <section class="flex flex-col w-full">
    <div class="flex">
      <button
        class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-t-lg hover:bg-white/10 duration-200"
      >
        <PlusIcon class="h-6 w-6 text-white" />
      </button>
    </div>
    <div class="flex font-montserrat">
      <div
        class="flex flex-col w-1/2 border-site-gray border-y-2 border-l-2 border-r rounded-bl-lg"
      >
        <h3 class="text-center py-7 border-b-2 border-site-gray">Influx</h3>
        <div
          class="flex flex-col overflow-y-auto scrollbar-thumb-white scrollbar-track-black/70 scrollbar-thin h-[18rem]"
        >
          <div class="flex justify-between px-[10%] py-4 border-b border-site-gray">
            <p>Salary</p>
            <p class="font-thin text-site-green">+ 2000</p>
          </div>
          <div class="flex justify-between px-[10%] py-4 border-b border-site-gray">
            <p>Salary</p>
            <p class="font-thin text-site-green">+ 2000</p>
          </div>
        </div>
        <button
          class="flex justify-center items-center py-4 border-t border-site-gray rounded-bl-lg hover:bg-white/10 duration-200"
        >
          <PlusIcon class="h-6 w-6" />
        </button>
      </div>
      <div class="flex flex-col w-1/2 border-site-gray border-y-2 border-r-2 border-l rounded-r-lg">
        <h3 class="text-center py-7 border-b-2 border-site-gray">Outflux</h3>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
</script>
