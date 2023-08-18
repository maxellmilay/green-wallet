<template>
  <div
    class="flex h-[100dvh] w-full justify-center items-center top-0 bg-black/80 fixed md:absolute"
  >
    <div class="w-[25rem] lg:w-[35rem]">
      <div class="p-5 md:p-10 bg-black rounded-lg border">
        <div class="flex w-full justify-end">
          <button class="bg-site-red text-black rounded-full" @click="closeModal">
            <XMarkIcon class="h-6 w-6 p-1" />
          </button>
        </div>
        <div class="flex flex-col">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { XMarkIcon } from '@heroicons/vue/24/solid';

const emit = defineEmits(['closeModal']);

const closeModal = () => {
  emit('closeModal');
};
</script>
