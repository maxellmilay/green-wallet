<template>
  <RouterLink
    :to="Route"
    class="flex items-center w-full gap-3 rounded px-8 py-3 text-white hover:bg-site-primary hover:-translate-y-2 hover:text-black duration-300"
  >
    <Icon class="aspect-square h-4 md:h-6" />
    <p class="text-smmd:text-lg font-montserrat">{{ name }}</p>
  </RouterLink>
</template>
<script setup lang="ts">
import { FunctionalComponent, HTMLAttributes, VNodeProps, computed, markRaw } from 'vue';
import { RouteLocationRaw } from 'vue-router';
import Routes from '../enums/routes';

const { icon, name, route } = defineProps({
  icon: Object as () => FunctionalComponent<HTMLAttributes & VNodeProps>,
  name: String,
  route: Object as () => RouteLocationRaw,
});

const Icon = computed(() => {
  if (icon) {
    return markRaw(icon);
  }
});

const Route = computed(() => {
  if (route) {
    return route;
  } else {
    return Routes.DEFAULT;
  }
});
</script>
