+++
title = "Customizing zola with macros and shortcodes"
description = "Showcasing some useful macros and shortcodes"
date = 2022-01-09
updated = 2022-01-13
draft = true
[taxonomies]
tags = ["build", "website", "remembrall"]
+++

I write most of my content in markdown, there's a lot that you can get out of the common mark specification. But sometimes you just need a little something that's custom. There are other specifications of markdown that have extensions that provide richer functionality - extended tables, math rendering, diagramming, etc. The problem is that they use a custom renderer, so your content is now locked-in with that renderer and will no longer be portable.

In the context of building websites with zola we have a great feature called shortcodes. While it still has the same pitfalls of using a custom renderer, for the context of building static websites the concept of shortcodes is quite similar across template engines.

Shortcodes are little snippets or functions written in html or markdown that can take some input parameters and generate html that gets inserted in place of the shortcode in your content. This is present in many template engines like tera and jinja. And is really similar conceptually to a re-usable component.

Here are some shortcodes that I wrote:

#### `csv2table(path: str)`

This shortcode takes a path to a CSV file and renders it as a html table. Nothing fancy just a straightforward html table. But really convenient when you want to display that data file or extract as a html table. Also, if paired with a javascript library that improves tables then it's a win-win.

{{ code(path="templates\shortcodes\csv2table.html", syntax="html") }}

Some extras could be:

- a `limit: int` parameter that renders only the specified number of lines in a tall data file
- a `highlight: array[str]` and `highlight_class: str` parameters that inject a the specified class list on the <td> that match any item in the specified array

Features grow with the requirements and it's often best to keep it as simple as possible.
