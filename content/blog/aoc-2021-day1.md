+++
title = "Advent of Code / 2021 / Day 1"
description = "Solving day 1 from AoC 2021"
date = 2021-12-06
updated = 2022-01-06
[taxonomies]
tags = ["puzzle", "aoc"]
+++

Let's solve [day 1](https://adventofcode.com/2021/day/1)

### Part 1

#### Problem

The input is a list of integers. The result is the number of sequence pairs that are increasing.

#### Crux

The idea here is to keep track of the number of increasing sequential numbers. Using `zip` we can iterate simultaneously through the list slices, one from the start till the penultimate element and the other from the second element till the end. Then we just need to check if the element is greater than it's previous element to increment a counter.

#### Solution

```py
def solution1(inputs: list[int]) -> int:
    counter = 0
    for elem, prev in zip(inputs[1:], inputs[:-1]):
        if elem > prev:
            counter += 1

    return counter
```

### Part 2

#### Problem

The problem is almost the same except we need to consider 3 elements summed and the next 3 elements. This combination of sequential elements is a window. In this case a window of size 3. The task is simplified since we only need the sum of the window.

#### Crux

The main idea is to define the windows. The rest of the solution works on the windows instead.

#### Solution

```py
def solution2(inputs: list[int]) -> int:
    window_size = 3
    final_window_index = len(inputs) - window_size + 1

    windows = [sum(inputs[i:i+window_size])
               for i in range(final_window_index)]

    return solution1(windows)
```
