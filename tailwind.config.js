// const remark = require('remark')

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
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
