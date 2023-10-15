# New Year Chaos Solutions

## Description

This repository contains two solutions for the HackerRank's "New Year Chaos" problem. The problem revolves around understanding the minimum number of bribes that took place to reach a given queue state.

challenge description: [new-year-chaos](https://www.hackerrank.com/challenges/new-year-chaos) 


## Solution 1: O(n) Approach

The first solution leverages a simple iterative method to determine the number of bribes. It examines each person in the queue and compares their current position to their original position. If the difference exceeds 2, the situation is deemed "Too chaotic". Otherwise, it counts the number of people who had to be bribed to get to the current state.

[View Code: solution1.py](./solution1.py)


## Solution 2: Fenwick Tree (O(n log n) Approach)

The second solution employs a Fenwick Tree (or Binary Indexed Tree) to efficiently compute the number of bribes. The Fenwick Tree is particularly useful for problems that involve prefix sums or cumulative frequencies. In this solution, we utilize the tree to keep track of the number of people who have been processed and use it to calculate the number of bribes efficiently.

[View Code: solution2.py](./solution2.py)

---

Please refer to the respective Python files for a detailed understanding of each solution. If you have any improvements or suggestions, feel free to contribute!

---
