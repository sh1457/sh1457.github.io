+++
title = "Building static websites - Part 3"
slug = "building-static-websites-part-3"
date = 2021-06-21
+++

## Static website

A static website is collection on content that changes so infrequently that the content can be served without any dynamic content or integrating with APIs. Many
popular choices are technical documentation, personal websites, small websites, blogs. These sites have little to no need to have any dynamic content. They can
be built from hand using a bunch of documents that fill known content into predefined templates. This allows the creator to focus on content first after
building simple skeleton templates.

## Static website generators

There are many tools nowadays that bootstrap the process. Jekyll..Hugo..Zola..Pelican - these are implemented in different programming languages -
Ruby..Go..Rust..Python. But at the heart provides so much configuration that there is minimal effort to code, unless one requires custom features.

The mechanism in which they work are similar. First one initializes the tool, this creates a skeleton project structure with basic style templates and a
designated folder for content. The tools aim to separate the content from the styling.

Content can be created in the form of text documents in markdown formats for example.

Then there is a build process, the tool takes the content and templates and binds them together to form the resultant HTML file. This file can then be opened on
the browser or served on a web server to be available on the internet.

## Blogging

Blogging is a window into a person's mind. It brings out a person's ability to collect their thoughts and present them in a structured body. It achieves
multiple objectives:

- Writing effectively
- Structuring and retrieving thoughts
- Presenting an idea or concept

---

## Zola

Zola is a fantastic static site generator which provides a lot of flexibility in developing and organizing websites. It's built in rustlang and uses the Tera
template language for extensible templates. After setting up templates, it makes it real easy to focus on content in markdown.

## Tailwind

Tailwind is a utilitarian css framework that's been taking over the internet recently. The fact that any/most requirements can be satisfied with their pre-built
classes is amazing. Makes it even better that the css is now maintained in the html. No need to have multiple tabs ever again.
