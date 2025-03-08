from typing import List


def generate_conterexample() -> List[int]:
    return [1, 2, 3]


def solution(prices: List[int]) -> int:
    """
    Introduction

    Consider the following problem:

    You are given a record showing an investment asset's historical prices from
    the last N days.
    Assume you started with one asset and could hold at most one at a time.
    You could choose to sell the asset when you had it, and if you did not have
     the asset, you could buy it (assume you had infinite money available).
    What is the maximum income you could have made?

    For example, for `prices` = [2, 4, 1, 5, 7], the maximum possible income is 10.
    You could sell the asset on the second day (for 4), buy it on the third (for 1)
    and sell it again on the last day (for 7).
    The income would be 4 - 1 + 7 = 10.

    Write an efficient algorithm for the following assumptions:
        - N is an integer within the range [1..100,000]
        - each element of array `prices` is an integer within the range [1..10,000].

    Task

    You are given a function `solution` that was generated and commented by a
    generative AI tool.
    The function `solution` takes an array `prices` of N integers representing a
    record of prices over the last N days, and attempts to solve the problem stated
     above.
    Currently, does not solve the problem correctly.
    Your task is to:
        - provide a test case on which the given function `solution` returns incorrect
         output, using the `generate_counterexample` function to return the test case
         (worth 35% of the total number of points);
        - find and fix the errors in the provided `solution` function (worth 65%).

    Examples
        1. The test validates if the counterexample provided using the
        `generate_conterexample` function is in the correct format.
        Note that it does not check if the provided function `solution` returned an
        incorrect output on that test.
        2. For `prices` = [2, 4, 1, 5, 7], the `solution` function should return 10.
    """
    prices = [0] + prices + [0]

    def should_sell(i):
        return prices[i] > prices[i - 1] and prices[i] >= prices[i + 1]

    def should_buy(i):
        return prices[i] < prices[i - 1] and prices[i] <= prices[i + 1]

    want_to_sell = True
    total_profit = 0

    for i in range(1, len(prices) - 1):
        if want_to_sell and should_sell(i):
            total_profit += prices[i]
            want_to_sell = False
        elif not want_to_sell and should_buy(i):
            total_profit -= prices[i]
            want_to_sell = True
    return total_profit
