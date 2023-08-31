<template>
  <img :src="ImagePath.LOGIN_LOGO" alt="Login" class="aspect-square mb-5" />
  <h1 class="font-karla text-4xl font-thin mb-10">Green Wallet</h1>
  <button
    class="font-karla text-xl text-site-green font-thin rounded-[0.625rem] border-[2px] border-site-green px-10 py-2 hover:bg-site-green hover:text-black hover:font-bold duration-300"
    @click="loginClick"
  >
    Login with Google
  </button>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router';
import ImagePath from '../enums/imagePath';

const router = useRouter();

const loginClick = () => {
  const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
  const redirectUri = 'social_auth/google/';

  const scope = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
  ].join(' ');

  const params = {
    response_type: 'code',
    client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
    redirect_uri: `${import.meta.env.VITE_API_BASE_URL}/${redirectUri}`,
    prompt: 'select_account',
    access_type: 'offline',
    scope
  };

  const urlParams = new URLSearchParams(params).toString();

  window.location.href = `${googleAuthUrl}?${urlParams}`;
};
</script>
