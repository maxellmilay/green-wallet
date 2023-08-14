<template>
  <div class="flex h-full">
    <SideMenu v-if="pathName !== Routes.LOGIN" />
    <main class="flex flex-col items-center grow" :class="loginAlign">
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

const loginAlign = computed(() => {
  if (pathName.value === Routes.LOGIN) {
    return 'justify-center';
  } else {
    return '';
  }
});
</script>

