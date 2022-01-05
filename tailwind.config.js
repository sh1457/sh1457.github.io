// const remark = require('remark')
const colors = require('tailwindcss/colors')

module.exports = {
  content: {
    files: ['./templates/**/*.html', './content/**/*.{html,md}'],
    // transform: {
    //   md: (content) => {
    //     return remark().process(content)
    //   },
    // },
  },
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      white: colors.white,
      black: colors.black,
      primary: colors.rose,
      secondary: colors.orange,
      nuetral: colors.zinc,
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
