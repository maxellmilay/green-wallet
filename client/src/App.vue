<template>
  <SideMenu v-if="pathName !== Routes.LOGIN" />
  <main class="flex flex-col items-center grow" :class="routeClass">
    <Suspense>
      <RouterView />
    </Suspense>
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
  } else if (pathName.value === Routes.TRANSACTIONS) {
    return 'justify-center py-10 md:py-0 md:h-[100dvh] items-center px-[10%] relative';
  } else {
    return 'h-full';
  }
});
</script>
