+++
title = "Advent of Code"
description = "(Re)visiting advent of code"
date = 2021-12-05
updated = 2022-01-06
[taxonomies]
tags = ["puzzle", "aoc"]
+++

I've known about [Advent of Code](https://adventofcode.com) for a around 3 years now. I try to solve it but somehow lose steam partway through. Mostly because it's december and the holiday season is ripe with distractions and other plans.

<!-- more -->

Here's what it is for the uninitiated (_ripped straight from their about page_):

> Hi! I'm Eric Wastl. I make Advent of Code. I hope you like it! I also made Vanilla JS, PHP Sadness, and lots of other things. You can find me on Twitter and GitHub.
>
> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.
>
> You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

I mostly solve these kinds of challenges with [python](https://www.python.org). Python is an interpreted language but is able to express intuitive and readable solutions. I do plan to try at least one or more compiled language as well as a challenge to myself. But it has been many years since I dealt with low level memory management and pointers. But nonetheless [zig](https://ziglang.org) and [rust](https://www.rust-lang.org) [go](https://go.dev) seem very promising.

Over the years, I built a toolchain to effectively organize and solve such programming challenges. I have certain helpers to quickly debug/test solutions.

Advent of Code is different in the sense that you are provided a unique input set and simply need to provide the result to that given input set. Hence we can be a bit more relaxed about the solution time constraints. Although as mentioned by the creator there is always a solution that will complete in under 15s even on older hardware. The problems are designed in such a way that only solutions with the right time complexity can provide an answer in reasonable time, especially in the later stage.

Some useful helper functions are:

- a function that takes in the solution function, [list of] input and [list of] expected output and returns [list of] result

```py
def solve(function: Callable,
          inputs: list[Any],
          expected_outputs: list[Any]) -> list[Any]:
    for inp, exp_out in zip(inputs, expected_outputs):
        out = function(inp)
        assert out == exp_out, "Failed!"
```

- a function that times the solution function

```py
def log_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = end_time - start_time
        msg = (f"Function {func.__name__!r} executed"
               f" in {duration:.4f}s")
        print(msg)
        return result
    return wrapper
```

- a function that profiles the solution function

I have not yet implemented such a function. While I have used the profiler present in the standard library `cprofile`, I have yet to use it extensively in the context of programming challenges. Most of my approach depends on estimating the time complexity and optimizing the solution (almost using only the standard library). Very rarely would I need to run a profiler to see where the slowness is coming from.

These are solution independent and usable across challenges. Many end up creating a similar toolchain.
