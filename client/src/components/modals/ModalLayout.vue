<template>
  <div
    class="flex h-[100dvh] w-full justify-center items-center top-0 bg-black/80 fixed md:absolute"
  >
    <div class="w-[25rem] lg:w-[35rem]">
      <div class="p-5 md:p-10 bg-black rounded-lg border"><slot /></div>
    </div>
  </div>
</template>
<script setup lang="ts"></script>
