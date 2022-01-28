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
            maxWidth: '80ch',
            lineHeight: '1.5',
            'code::before': {
              content: 'none',
            },
            'code::after': {
              content: 'none',
            },
          },
        },
      }),
      keyframes: {
        smoke: {
          '0%': { transform: 'translate(0, 0) rotate(0deg) scale(0.9)' },
          '25%': { transform: 'translate(5, 5) rotate(90deg) scale(0.75)' },
          '50%': { transform: 'translate(0, 0) rotate(180deg) scale(0.8)' },
          '75%': { transform: 'translate(5, 5) rotate(270deg) scale(0.75)' },
          '100%': { transform: 'translate(0, 0) rotate(360deg) scale(0.9)' },
        },
      },
      animation: {
        smoke: 'smoke 2s linear infinite',
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
