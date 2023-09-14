<template>
  <button
    class="flex justify-between px-[10%] py-4 border-b border-site-gray text-xs md:text-base hover:bg-white/10 duration-200"
  >
    <p>{{ name }}</p>
    <p class="font-thin" :class="isPositive ? 'text-site-green' : 'text-site-red'">
      {{ amountSign }} {{ Math.abs(amount) }}
    </p>
  </button>
</template>
<script setup lang="ts">
import { computed, ref } from 'vue';

const isPositive = ref(false);

const { name, amount } = defineProps({
  name: { type: String, required: true },
  amount: { type: Number, required: true },
});

const amountSign = computed(() => {
  if (amount >= 0) {
    isPositive.value = true;
    return '+';
  } else {
    isPositive.value = false;
    return '-';
  }
});
</script>
