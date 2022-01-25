const colors = require('tailwindcss/colors')

module.exports = {
  content: {
    files: ['./templates/**/*.html', './content/**/*.{html,md}'],
  },
  darkMode: 'class',
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      white: colors.white,
      black: colors.black,
      primary: colors.rose,
      secondary: colors.orange,
      neutral: colors.neutral,
    },
    extend: {
      typography: (theme) => ({
        DEFAULT: {
          css: {
            a: {
              color: theme('colors.primary.600'),
            },
          },
        },
        dark: {
          css: {
            a: {
              color: theme('colors.secondary.600'),
              },
            },
        },
      }),
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
