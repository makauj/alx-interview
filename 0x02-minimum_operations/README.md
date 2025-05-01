# Minimum Operations

## Task

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0
**Example:**

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

## Solution

**What I understand:**

- we start with one `H`
- I can only use **Copy All** (copies all the content in the file) and **Paste** (pastes what was copied)
- the goal is to reach excatly `n` characters with the fewest number of operations

***Key Insight:***

The problem is essentially about factorizing n. The optimal strategy is to build n by multiplying smaller numbers together, and the operations are:

- 1 operation for Copy All
- Then multiple operations for Paste to multiply.

So, for every factor of n, we simulate doing:

- 1 Copy All
- (factor - 1) Pastes
    → total of factor operations to multiply the current string length by factor.

Algorithm:

1. Start with the smallest factor of n (starting from 2).
2. While n is divisible by that factor:

    - Add that factor to the total operations.
    - Divide n by that factor.

3. Repeat for the next factor.

This way, we reduce n using its smallest factors first, minimizing the total number of operations.
