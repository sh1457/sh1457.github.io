const colors = require('tailwindcss/colors')

module.exports = {
  content: {
    files: ['./templates/**/*.html', './content/**/*.{html,md}'],
  },
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      white: colors.white,
      black: colors.black,
      primary: colors.rose,
      secondary: colors.orange,
      neutral: colors.zinc,
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
