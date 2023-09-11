<template>
  <FluxLayout
    :title="fluxType"
    class-name="mb-5 md:mb-0 md:border-r rounded-r-lg rounded-bl-lg md:rounded-bl-lg md:rounded-r-none md:rounded-tl-none"
  />
</template>

<script setup lang="ts">
import FluxLayout from '../FluxLayout.vue';
import Types from '../../enums/types';

const { fluxType } = defineProps({
  fluxType: { type: String, required: true },
});
</script>
