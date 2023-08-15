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
        menuClose: {
          '0%': { width: '17rem' },
          '100%': { width: 0 },
        },
        menuOpen: {
          '0%': { width: 0 },
          '100%': { width: '17rem' },
        },
        toggleClose: {
          '0%': { left: '17rem' },
          '100%': { left: 0 },
        },
        toggleOpen: {
          '0%': { left: 0 },
          '100%': { left: '17rem' },
        },
      },
      animation: {
        'menu-close': 'menuClose 1s forwards',
        'menu-open': 'menuOpen 1s forwards',
        'toggle-close': 'toggleClose 1s forwards',
        'toggle-open': 'toggleOpen 1s forwards',
      },
    },
  },
  plugins: [require('tailwind-scrollbar')],
};

