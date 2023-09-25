/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  content: [
          './templates/**/*.html'
  ],
  theme: {
    extend: {},
     screens: {
      'xs': '552px',
      ...defaultTheme.screens,
    },
  },
  plugins: [],
}


