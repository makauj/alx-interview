#!/usr/bin/python3
"""
Given a pile of coins of different values, 
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total.
    If it is not possible to meet the total, returns -1.
    """
    if total <= 0:
        return 0
    # Initialize the dp array with total+1 (a value greater than any possible answer)
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Bottom-up DP approach
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] <= total else -1
