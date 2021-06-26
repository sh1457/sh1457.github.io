# [sh1457.github.io](https://sh1457.github.io) Personal Website and Blog

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

Creates the default config `config.toml` by default

`zola init`

#### Build

Builds the site into a folder `public` by default

`zola build`

#### Build and serve

Builds and serves the site locally

`zola serve`

### Using tailwindcss CLI

Rather than using tailwind as a PostCSS plugin, we are using it as a standalone tool

#### Init

Creates the default config `tailwind.config.js` by default

`npx tailwindcss init`

#### Build css

We are using a custom css file as input to build at `src/tailwind.css` We will be serving the built css file at the
static folder in zola. `static/css/tailwind.css`

`npx tailwindcss -i src/tailwind.css -o static/css/tailwind.css`

## Deploy

We are using this GitHub action [github.com/shalzz/zola-deploy-action](https://github.com/shalzz/zola-deploy-action) to
build the site from the `master` branch and deploy to the `gh-pages` branch.

Github then serves the content from the `gh-pages` branch at the respective domain specified in the settings.

## Links

- [Zola](https://www.getzola.org/)
- [Tailwind](https://tailwindcss.com/)
- [github.com/shalzz/zola-deploy-action](https://github.com/shalzz/zola-deploy-action)
