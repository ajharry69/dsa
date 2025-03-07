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
