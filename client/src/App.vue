<template>
  <SideMenu v-if="pathName !== Routes.LOGIN" />
  <main class="flex flex-col items-center grow" :class="routeClass">
    <RouterView />
  </main>
</template>

<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router';
import SideMenu from './components/SideMenu.vue';
import { computed } from 'vue';
import Routes from './enums/routes';

const route = useRoute();

const pathName = computed(() => route.path);

const routeClass = computed(() => {
  if (pathName.value === Routes.LOGIN) {
    return 'justify-center h-[100dvh]';
  } else if (pathName.value === Routes.PROFILE) {
    return 'justify-center gap-10 h-[100dvh]';
  } else {
    return 'h-full';
  }
});

const routeContainerClass = computed(() => {
  if (pathName.value === Routes.PROFILE) {
    return 'h-[100dvh]';
  } else {
    return 'h-full';
  }
});
</script>

