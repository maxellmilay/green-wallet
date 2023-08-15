<template>
  <div
    class="flex items-center gap-x-4 hover:bg-white bg-site-green duration-300 rounded-xl text-black py-6 px-10 w-fit"
  >
    <Icon class="h-8 w-8" />
    <div class="flex flex-col gap-y-1 font-montserrat">
      <p class="text-center">{{ name }}</p>
      <p class="font-semibold">&#8369; {{ value }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { FunctionalComponent, VNodeProps, HTMLAttributes, computed, markRaw } from 'vue';

const { icon, name, value } = defineProps({
  icon: Object as () => FunctionalComponent<HTMLAttributes & VNodeProps>,
  name: String,
  value: Number,
});

const Icon = computed(() => {
  if (icon) {
    return markRaw(icon);
  }
});
</script>
