+++
title = "Building static websites"
slug = "building-static-websites"
date = 2021-06-18
updated = 2022-01-06
+++

A static website is collection of content that does not change and can be served completely to the client. Such websites
are easy to download for offline browsing.

<!-- more -->

Examples of such sites are documentation, small websites, blogs, book as a website. These sites have little to no
dynamic content - content that changes at a rate where a server would be required to serve it.

#### Static website generators

Static website generators are tools that build static websites. There are many tools nowadays implemented in various
languages both interpreted and compiled. Building static websites is not a critical task in the view of the user. That's
why tool performance is not the main criteria for choosing the right tool. But nonetheless the authors/creators would
appreciate fast builds and deploys.

| Tool    | Lang   |
| ------- | ------ |
| Jekyll  | ruby   |
| Hugo    | go     |
| Zola    | rust   |
| Pelican | python |

But at the heart each tool provides configuration to create flexible site structures. The tools aim to separate the
content from the styling. Content can be created in the form of text documents in markdown formats for example.

The have similar mechanics.

1. Initialize the tool
   - create a skeleton folder structure
2. Build templates
3. Write content

Then there is a build process, the tool takes the content and templates and binds them together to form the resultant
HTML file. This file can then be opened on the browser or served on a web server to be available on the internet.

[Zola](https://www.getzola.org/) is a fantastic static site generator which provides a lot of flexibility in developing
and organizing websites. It's built in rust and uses the tera template language. After creating templates, it makes it
real easy to focus on content in markdown.

[Tailwind](https://tailwindcss.com/) is a utilitarian css framework that's been taking over the internet recently. The
fact that any/most requirements can be satisfied with their pre-built classes is amazing. Makes it even better that the
css is now maintained in the html. No need to have multiple tabs to web design ever again.
