/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js, jsx, ts, tsx, html}',
  ],
  theme: {
    extend: {
      keyframes: {
        customPing: {
          '0%': { transform: 'scale(1)', opacity: '1' },
          '75%, 100%': { transform: 'scale(1.5)', opacity: '0' }, // make radius a bit smaller
        },
      },
      animation: {
        customPing: 'customPing 1s cubic-bezier(0, 0, 0.2, 1) 8', // will ping 8 times then stop
      },
    },
  },
  plugins: [],
};
