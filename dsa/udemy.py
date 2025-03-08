def remove_element(nums: list[int], val: int):
    """
    Given a list of integers `nums` and an integer `val`, write a function `remove_element`
    that removes all occurrences of `val` in the list in-place and returns the new length
    of the modified list.

    The function should not allocate extra space for another list; instead, it should
    modify the input list in-place with O(1) extra memory.

    Input:
        - A list of integers `nums`.
        - An integer `val` representing the value to be removed from the list.

    Output:
        - An integer representing the new length of the modified list after removing all
        occurrences of `val`.

    Constraints:
        - Do not use any built-in list methods, except for `pop()` to remove elements.
        - It is okay to have extra space at the end of the modified list after removing
         elements.
    """

    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def find_max_min(nums):
    """
    Write a Python function that takes a list of integers as input and returns a tuple
    containing the maximum and minimum values in the list.
    """
    small = big = nums[0]
    for n in nums:
        big = max(big, n)
        small = min(small, n)
    return big, small


def find_longest_string(strings: list[str]):
    longest = ''

    for string in strings:
        if len(string) > len(longest):
            longest = string

    return longest


def remove_duplicates(nums):
    """
    This code defines a function remove_duplicates that takes a sorted list of
    integers called nums as input and rearranges it in-place to move unique
    elements to the beginning, followed by duplicate elements. The function
    returns the new length of the list containing only unique elements.
    """
    if not nums:
        return 0

    write_pointer = 1

    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    return write_pointer


def max_profit(prices):
    """
    You are given a list of integers representing stock prices for a certain company over
    a period of time, where each element in the list corresponds to the stock price for
    a specific day.

    You are allowed to buy one share of the stock on one day and sell it on a later day.

    Your task is to write a function called max_profit that takes the list of stock prices
    as input and returns the maximum profit you can make by buying and selling at the
    right time.

    Note that you must buy the stock before selling it, and you are allowed to make only
    one transaction (buy once and sell once).

    Constraints:

    Each element of the input list is a positive integer representing the stock price
    for a specific day.

    Function signature: def max_profit(prices):

    Example:

    Input: prices = [7, 1, 5, 3, 6, 4]
    Function call: profit = max_profit(prices)
    Output: profit = 5

    Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1)
     and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
    """
    if not prices:
        return 0

    min_price = prices[0]  # Initialize with the first day's price
    max_profit_val = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Update the minimum price if a lower price is found
        else:
            profit = price - min_price
            max_profit_val = max(max_profit_val, profit)

    return max_profit_val


def rotate(nums, k):
    """
    You are given a list of n integers and a non-negative integer k.

    Your task is to write a function called `rotate` that takes the list of integers and an
    integer `k` as input and rotates the list to the right by `k` steps.

    The function should modify the input list in-place, and you should not return anything.

    Constraints:
        1. Each element of the input list is an integer.
        2. The integer k is non-negative.
    """
    n = len(nums)
    if n < 2:
        return

    steps = 0
    # this optimises for:
    #   1. n-th time rotation where the item positions are will not change
    #   2. rotations greater than the length eventually lead rotations between 0 and n - 1
    # For example, rotate [1, 2, 3, 4, 5], 6 times
    #
    # [5, 1, 2, 3, 4]; 1st
    # [4, 5, 1, 2, 3]; 2nd
    # [3, 4, 5, 1, 2]; 3rd
    # [2, 3, 4, 5, 1]; 4th
    # [1, 2, 3, 4, 5]; 5th
    #
    # [5, 1, 2, 3, 4]; 6th
    # notice than the 6th rotation is a repeat of the 1st.
    rotations = k % n
    while steps < rotations:
        i = n - 1
        last = nums[i]
        while i > 0:
            nums[i] = nums[i - 1]
            i -= 1
        nums[0] = last
        steps += 1
