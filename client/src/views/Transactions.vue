<template>
  <header class="flex flex-col md:flex-row justify-between items-center w-full mb-5">
    <h2 class="font-karla text-2xl md:text-4xl">Transactions</h2>
    <div class="flex flex-col items-center md:items-end">
      <p class="font-montserrat text-2xl text-site-green">3000</p>
      <p class="font-karla font-thin text-xs md:text-base">Balance</p>
    </div>
  </header>
  <section class="flex flex-col w-full">
    <div class="flex justify-center md:justify-start">
      <button
        class="flex px-4 py-2 border-t-2 border-x-2 border-site-gray rounded-t-lg hover:bg-white/10 duration-200"
      >
        <PlusIcon class="h-6 w-6 text-white" />
      </button>
    </div>
    <div class="flex flex-col md:flex-row font-montserrat mb-5">
      <Influx />
      <Outflux />
    </div>
    <div class="flex justify-center gap-8">
      <button
        class="border-2 text-white border-white rounded-lg px-6 py-3 bg-black hover:bg-white/10 duration-200"
      >
        Export
      </button>
      <button
        class="border-2 text-site-red border-site-red rounded-lg px-6 py-3 bg-black hover:bg-site-red/20 hover:text-white duration-200"
      >
        Reset
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/solid';
import Influx from '../components/Influx.vue';
import Outflux from '../components/Outflux.vue';
</script>
