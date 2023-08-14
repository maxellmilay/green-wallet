/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'site-primary': '#00EFC5',
        'site-green': '#9AE576',
        'site-red': '#E57676',
      },
      fontFamily: {
        karla: ['Karla', 'serif'],
        montserrat: ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [],
};


