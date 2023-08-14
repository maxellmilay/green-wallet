<template>
  <aside class="flex">
    <div
      class="p-10 border-r border-site-gray duration-500 overflow-hidden relative"
      :class="{ 'ml-[-17.51rem]': !isMenuOpen, 'display-hidden': isTransitionDone }"
      @after-enter="setTransitionDone"
    >
      <header class="flex flex-col items-center">
        <img src="/images/menu-icon.png" alt="Menu" class="p-5 aspect-square h-[10rem]" />
        <h1 class="text-site-primary text-3xl font-karla mb-7">Green Wallet</h1>
        <nav class="flex flex-col w-full gap-7">
          <RouterLink
            to="/profile"
            class="flex w-full gap-3 rounded px-8 py-3 text-white hover:bg-site-primary hover:text-black duration-300"
          >
            <UserCircleIcon class="h-6 w-6" />
            <p class="text-lg font-montserrat">Profile</p></RouterLink
          >
          <RouterLink
            to="/dashboard"
            class="flex w-full gap-3 rounded px-8 py-3 text-white hover:bg-site-primary hover:text-black duration-300"
          >
            <ComputerDesktopIcon class="h-6 w-6" />
            <p class="text-lg font-montserrat">Dashboard</p></RouterLink
          >
          <RouterLink
            to="/login"
            class="flex w-full gap-3 rounded px-8 py-3 text-white hover:bg-site-primary hover:text-black duration-300"
          >
            <ArrowLeftCircleIcon class="h-6 w-6" />
            <p class="text-lg font-montserrat">Logout</p></RouterLink
          >
        </nav>
      </header>
    </div>
    <div class="flex items-center">
      <button
        class="py-3 px-1 border-y bg-black hover:bg-zinc-900 duration-200 border-r border-site-gray rounded-r-[0.3rem]"
        @click="closeMenuClick"
      >
        <ChevronLeftIcon class="text-white h-6 w-6" />
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import {
  ChevronLeftIcon,
  UserCircleIcon,
  ComputerDesktopIcon,
  ArrowLeftCircleIcon,
} from '@heroicons/vue/24/solid';
import { ref, watch } from 'vue';

const isMenuOpen = ref(true);
const isTransitionDone = ref(false);

const closeMenuClick = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const setTransitionDone = () => {
  isTransitionDone.value = true;
};

watch(isMenuOpen, (newValue) => console.log(newValue));
</script>

<style scoped>
.display-hidden {
  display: none;
}
</style>
