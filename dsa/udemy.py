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
    longest = ""

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


def rotate_1(nums, k):
    n = len(nums)
    if n == 0:
        return
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


def max_subarray(nums):
    """
    Given an array of integers nums, write a function max_subarray(nums) that finds
     the contiguous subarray (containing at least one number) with the largest sum
     and returns its sum.

    Remember to also account for an array with 0 items.

    Args:
        nums:  A list of integers.

    Output:
        An integer representing the sum of the contiguous subarray with the largest sum.

    Example:
    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    Output: 6
    Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
    """

    n = len(nums)

    if n == 0:
        return 0, []

    maximum = nums[0]
    i = 0
    x, y = i, i + 1

    while i < n:
        j = i + 1
        s = nums[i]
        while j < n:
            if s > maximum:
                maximum = s
                x, y = i, j
            s += nums[j]
            j += 1
        # account for the sum that includes the last number
        if s > maximum:
            maximum = s
            x, y = i, j
        i += 1

    return maximum, nums[x:y]


def max_subarray_1(nums):
    n = len(nums)
    if n == 0:
        return 0

    maximum = nums[0]
    i = 0

    while i < n:
        j = i + 1
        s = nums[i]
        while j < n:
            maximum = max(maximum, s)
            s += nums[j]
            j += 1
        # account for the sum that includes the last number
        maximum = max(maximum, s)
        i += 1

    return maximum


def max_subarray_2(nums):
    """
    This code implements the Kadane's algorithm to find the maximum subarray sum.

    By using the Kadane's algorithm, this code efficiently finds the maximum
    subarray sum with a linear time complexity of O(n), where n is the length
    of the input list nums.
    """
    # This line checks if the input list nums is empty. If it's empty, the
    # function returns 0, as there's no subarray to calculate the sum.
    if not nums:
        return 0

    # Both max_sum and current_sum are initialized to the first element of the
    # input list nums. max_sum stores the maximum subarray sum found so far,
    # while current_sum keeps track of the maximum subarray sum ending at the
    # current position.
    max_sum = current_sum = nums[0]

    # The loop iterates through the remaining elements of the input list nums,
    # starting from the second element.
    for num in nums[1:]:
        # For each element num in the loop, this line updates the current_sum
        # by taking the maximum of two values: the current element itself
        # (num) and the sum of the current element and the previous current_sum.
        # This step ensures that if the previous current_sum is negative, it's
        # better to start a new subarray from the current element (since adding
        # a negative value to the current element would only decrease the sum).
        current_sum = max(num, current_sum + num)
        # After updating the current_sum, this line compares it with the
        # current max_sum. If the current_sum is greater than the max_sum,
        # it updates the max_sum value to be the current_sum. This way,
        # the max_sum variable always holds the maximum subarray sum found
        # so far.
        max_sum = max(max_sum, current_sum)

    # After iterating through all the elements in the input list, the function
    # returns the final value of max_sum, which represents the sum of the
    # contiguous subarray with the largest sum.
    return max_sum
