<template>
  <div class="flex justify-between px-[10%] py-4 border-b border-site-gray">
    <p>{{ description }}</p>
    <p class="font-thin" :class="isPositive ? 'text-site-green' : 'text-site-red'">
      {{ valueSign }} {{ value && Math.abs(value) }}
    </p>
  </div>
</template>
<script setup lang="ts">
import { computed, ref } from 'vue';

const isPositive = ref();

const { description, value } = defineProps({ description: String, value: Number });

const valueSign = computed(() => {
  if (!value) {
    return;
  }
  if (value >= 0) {
    isPositive.value = true;
    return '+';
  } else {
    isPositive.value = false;
    return '-';
  }
});
</script>
