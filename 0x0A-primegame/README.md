# The Prime Game

## 🧠 **Understanding the Game Rules**

1. You start with a list of numbers from `1` to `n`.
2. Players take turns. Maria always starts.
3. On a turn, a player:

   * Picks a **prime number** from the remaining numbers.
   * Removes that prime and all **its multiples** from the list.
4. If you **cannot pick a prime**, you lose.

So the **number of turns** in a game = number of primes ≤ `n`.

---

## 🔍 **Key Observations**

### ✅ 1. Primes Control the Game

Only prime numbers can be picked. All other numbers are irrelevant unless they are multiples of primes.

### ✅ 2. Each Prime Allows One Move

* Picking a prime removes it and its multiples (but you don't get extra turns).
* Example: Picking `2` in `[1,2,3,4,5]` removes `[2,4]`.
* You can't reuse removed numbers.

### ✅ 3. Players Play Optimally

* Both players will try to maximize their own chances of winning.
* The outcome depends purely on the **number of available prime numbers**, not on the exact numbers chosen.

---

## 📊 **So... Who Wins a Round?**

* If the number of primes ≤ `n` is:

  * **Odd** → Maria wins (she gets the last move).
  * **Even** → Ben wins (he gets the last move).

Why?

* Each player removes one prime and its multiples.
* Turns alternate.
* If there's an odd number of prime numbers, the **first player** gets more turns and makes the last move.

---

## 🚀 **Strategy for Solving the Problem**

### 1. For each round, find how many primes are ≤ `n`.

* Brute force for each `n` would be too slow.
* Use the **Sieve of Eratosthenes** once, up to the max value in `nums`.

### 2. Precompute number of primes up to each `i` from 1 to max(`nums`).

* Store in a `prime_counts` array so we can look up how many primes ≤ `n` in O(1).

### 3. Determine winner of each round:

* Use `prime_counts[n] % 2`:

  * Odd → Maria wins
  * Even → Ben wins

### 4. Count who won most rounds and return the result.

---

## 🧠 **Mental Model Example**

Let’s walk through one game, say `n = 5`.

* Numbers: `[1, 2, 3, 4, 5]`
* Primes: `[2, 3, 5]` → 3 primes → 3 turns
* Turn 1: Maria picks `2` → removes `2`, `4` → remaining `[1,3,5]`
* Turn 2: Ben picks `3` → removes `3` → remaining `[1,5]`
* Turn 3: Maria picks `5` → removes `5` → remaining `[1]`
* No primes left → Ben has no move → **Maria wins**

Odd number of primes → Maria wins.

---

## ✅ Summary of Core Insights

| Concept              | Insight                                            |
| -------------------- | -------------------------------------------------- |
| Primes               | Determine the number of turns                      |
| First Move Advantage | Maria wins if total prime count is odd             |
| Optimal Play         | Makes outcome predictable based on prime count     |
| Performance          | Precompute all primes up to max `n` for efficiency |
