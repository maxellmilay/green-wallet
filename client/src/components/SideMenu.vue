<template>
  <aside class="flex fixed z-20 bg-black md:relative h-[100dvh]">
    <div
      class="flex py-10 w-[17rem] h-full justify-center border-r border-site-gray overflow-hidden relative"
      :class="{
        'animate-menu-close': !isMenuOpen,
        'animate-menu-open': isMenuOpen && isLoadedOnce,
      }"
    >
      <header class="flex flex-col items-center">
        <img
          :src="ImagePath.MENU_ICON"
          alt="Menu"
          class="p-5 aspect-square h-[8rem] md:h-[10rem]"
        />
        <h1 class="text-site-primary text-2xl md:text-3xl font-karla mb-7">Green Wallet</h1>
        <nav class="flex flex-col w-full gap-5 md:gap-7">
          <MenuItem :icon="UserCircleIcon" name="Profile" :route="Routes.PROFILE" />
          <MenuItem :icon="ComputerDesktopIcon" name="Dashboard" :route="Routes.DASHBOARD" />
          <MenuItem :icon="BanknotesIcon" name="Transactions" :route="Routes.TRANSACTIONS" />
          <MenuItem :icon="ArrowLeftCircleIcon" name="Logout" :route="Routes.LOGIN" />
        </nav>
      </header>
    </div>
    <div
      class="flex absolute h-full items-center"
      :class="{
        'animate-toggle-close': !isMenuOpen,
        'animate-toggle-open': isMenuOpen && isLoadedOnce,
        'left-[17rem]': !isLoadedOnce,
      }"
    >
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
  BanknotesIcon,
} from '@heroicons/vue/24/solid';
import { ref } from 'vue';
import MenuItem from './MenuItem.vue';
import Routes from '../enums/routes';
import ImagePath from '../enums/imagePath';

const isMenuOpen = ref(false);
const isLoadedOnce = ref(false);

const closeMenuClick = () => {
  if (!isLoadedOnce.value) {
    isLoadedOnce.value = true;
  }
  isMenuOpen.value = !isMenuOpen.value;
};
</script>
