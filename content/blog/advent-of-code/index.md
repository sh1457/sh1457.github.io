+++
title = "Advent of Code"
slug = "advent-of-code"
date = 2021-12-05
update = 2021-12-05
+++

I will be making use of an interpreted language python and a compiled language zig to challenge myself. I have certain helper functions to quickly debug/test solutions. This is something I built over time solving various competitive coding problems.

AoC is different in the sense that you are provided the input list and need to simply provide the answer. Hence we can be a bit more relaxed about the solution time. So there are some differences in hardware to process the problems on. But at the end the problems are designed in such a way that only solutions with the right time somplexity can provide an answer in reasonable time, escpecially in the later stages.

Some useful helper functions would be
- a function that takes in the solution function, [list of] input and [list of] expected output and returns the results for each.
- a function that times the solution function
- a function that profiles the solution function

These are solution independent and usable across challenges. Most competitive programmers usually have their own toolchain on the same lines.
