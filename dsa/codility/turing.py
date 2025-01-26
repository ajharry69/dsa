def find_three_sum_1(arr):
    """
    Given an array of integers, return a set of 3 digits from the array whose sum equals zero.
    For example, given the array:
     1. [1, 2, 3, -3] should return [1, 2, -3]
     2. [1, 2, 3, 4, 5, 6, 7] should return []
    """
    size = len(arr)
    if size < 3:
        return []

    fi, si, ti = 0, 1, 2

    while True:
        if arr[fi] + arr[si] + arr[ti] == 0:
            return [arr[fi], arr[si], arr[ti]]

        if ti < size - 1:
            ti += 1
        elif si < size - 2:
            si += 1
        elif fi < size - 3:
            fi += 1
        else:
            break

    return []


def find_three_sum_2(nums):
    """
    Finds a set of three digits from the given array whose sum equals zero.

    Args:
      nums: A list of integers.

    Returns:
      A list containing the three digits that sum to zero, or an empty list if no such
      combination exists.
    """
    # nums.sort()  # Sort the array for efficient two-pointer approach
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second and third numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
