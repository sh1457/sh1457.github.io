+++
title = "Building static websites - Part 1"
slug = "building-static-websites-part-1"
date = 2021-06-18
+++

A static website is collection on content that does not changes and can be served without any dynamic content or API
integrations. Many popular examples of such sites are technical documentation, personal websites, small websites, blogs.

These sites have little to no dynamic content. They can be built using predefined content filled into predefined
templates. This allows focus on content after building simple templates.

## Static website generators

There are many tools nowadays. Jekyll..Hugo..Zola..Pelican - these are implemented in different programming languages -
Ruby..Go..Rust..Python. But at the heart each tool provides configuration to create flexible site structures.

The have similar mechanics. First one initializes the tool, this creates a skeleton project structure with basic style
templates and a designated folder for content. The tools aim to separate the content from the styling.

Content can be created in the form of text documents in markdown formats for example.

Then there is a build process, the tool takes the content and templates and binds them together to form the resultant
HTML file. This file can then be opened on the browser or served on a web server to be available on the internet.

## [Zola](https://www.getzola.org/)

Zola is a fantastic static site generator which provides a lot of flexibility in developing and organizing websites.
It's built in rustlang and uses the Tera template language for extensible templates. After setting up templates, it
makes it real easy to focus on content in markdown.

## [Tailwind](https://tailwindcss.com/)

Tailwind is a utilitarian css framework that's been taking over the internet recently. The fact that any/most
requirements can be satisfied with their pre-built classes is amazing. Makes it even better that the css is now
maintained in the html. No need to have multiple tabs ever again.
