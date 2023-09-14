<template>
  <div
    class="flex items-center justify-center lg:justify-start w-full bg-site-gray gap-10 px-10 py-6 rounded-xl"
  >
    <p
      class="text-xl font-thin min-w-[5rem] text-center lg:text-left"
      :class="amount >= 0 ? 'text-site-green' : 'text-site-red'"
    >
      {{ amount >= 0 ? '+' : '-' }} {{ Math.abs(amount) }}
    </p>
    <p class="grow hidden lg:block">{{ description }}</p>
  </div>
</template>

<script setup lang="ts">
const { amount, description } = defineProps({
  amount: { type: Number, required: true },
  description: { type: String, required: true },
});
</script>
