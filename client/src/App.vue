<template>
  <div class="flex" :class="routeContainerClass">
    <SideMenu v-if="pathName !== Routes.LOGIN" />
    <main class="flex flex-col items-center grow" :class="routeClass">
      <RouterView />
    </main>
  </div>
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
    return 'justify-center';
  } else if (pathName.value === Routes.PROFILE) {
    return 'justify-center gap-10';
  } else {
    return '';
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

