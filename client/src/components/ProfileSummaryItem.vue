<template>
  <div class="flex font-montserrat gap-4">
    <p class="font-extralight w-20 text-right">{{ name }}</p>
    <p class="font-bold w-24">&#8369; {{ value }}</p>
  </div>
</template>

<script setup lang="ts">
const { name, value } = defineProps({ name: String, value: Number });
</script>
