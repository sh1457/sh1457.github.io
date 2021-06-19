# (sh1457.github.io)[sh1457.github.io] Personal Website and Blog


## Installation

This is the install steps on Windows.

### Getting Zola
Zola is a rust package. We can get the latest binary from chocolatey

`choco install zola`

Update with choco

`choco update zola`

### Getting Tailwindcss
Tailwind is a nodejs package. We can use npm to install it

`npm install latest@tailwindcss latest@autoprefixer`

Same command updates as well

## Dev

### Using zola

#### Init
Creates the default config

`zola init`

#### Build
Builds the site

`zola build`

#### Build and serve
Builds and serves the site locally

`zola serve`

### Using tailwindcss CLI
Rather than using tailwind as a PostCSS plugin, we are using it as a standalone tool

#### Init
Creates the default config

`npx tailwindcss init`

#### Build css
We are using a custom css file as input to build at `src/tailwind.css`
We will be serving the built css file at the static folder in zola. `static/css/tailwind.css`

`npx tailwindcss -i src/tailwind.css -o static/css/tailwind.css`


## Links
