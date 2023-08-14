/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'site-primary': '#00EFC5',
        'site-green': '#9AE576',
        'site-red': '#E57676',
        'site-gray': '#262424',
      },
      fontFamily: {
        karla: ['Karla', 'serif'],
        montserrat: ['Montserrat', 'sans-serif'],
      },
      keyframes: {
        sidebar: {
          '0%': { marginLeft: '0' },
          '100&': { marginLeft: '-100px' },
        },
      },
      animation: {
        'sidebar-toggle': 'sidebar 2s ease 1',
      },
    },
  },
  plugins: [],
};

