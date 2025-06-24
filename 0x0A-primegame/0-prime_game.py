#!/usr/bin/python3
"""The Prime Game"""


def isWinner(x, nums):
    """
    Function that determines the winner of the Prime Game.
    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the numbers in each round.
    Returns:
        str: "Maria" if Maria wins, "Ben" if Ben wins, or None
                if there is a tie.
    """
    if x < 1 or not nums:
        return None

    n = max(nums)
    # Sieve of Eratosthenes
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Count primes up to each i
    prime_counts = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_counts[i] = count

    # Determine winner for each round
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if prime_counts[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
