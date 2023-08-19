<template>
  <button
    class="flex justify-between px-[10%] py-4 border-b border-site-gray text-xs md:text-base hover:bg-white/10 duration-200"
    @click="openTransactionItemModal"
  >
    <p>{{ description }}</p>
    <p class="font-thin" :class="isPositive ? 'text-site-green' : 'text-site-red'">
      {{ valueSign }} {{ Math.abs(value) }}
    </p>
  </button>
</template>
<script setup lang="ts">
import { computed, ref } from 'vue';
import { TItemPayload } from '../types/TTransaction';

const isPositive = ref();

const valueSign = computed(() => {
  if (value >= 0) {
    isPositive.value = true;
    return '+';
  } else {
    isPositive.value = false;
    return '-';
  }
});
</script>
