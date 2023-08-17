<template>
  <div
    class="flex items-center justify-center lg:justify-start w-full bg-site-gray gap-10 px-10 py-6 rounded-xl"
  >
    <p
      class="text-xl font-thin min-w-[5rem] text-center lg:text-left"
      :class="isPositive ? 'text-site-green' : 'text-site-red'"
    >
      {{ amountSign }} {{ amount && Math.abs(amount) }}
    </p>
    <p class="grow hidden lg:block">{{ description }}</p>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';

const { amount, description } = defineProps({
  amount: Number,
  description: String,
});

const isPositive = ref();

const amountSign = computed(() => {
  if (!amount) {
    return;
  }
  if (amount >= 0) {
    isPositive.value = true;
    return '+ ';
  } else {
    isPositive.value = false;
    return '- ';
  }
});
</script>
