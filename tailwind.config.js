/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  content: [
          './templates/**/*.html',
          './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
     screens: {
      'tab':'972px',
      'xs': '552px',
      ...defaultTheme.screens,
    },
  },
  plugins: [
    require('flowbite/plugin')
]

}


