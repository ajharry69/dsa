"""
def shift_zeros_to_the_end(nums: List[int]) -> None:
    zero_index = 0

    for curr_index in range(len(nums)):
        print("i =", curr_index, "; zi =", zero_index)
        print("\t", nums)
        if nums[curr_index] != 0:
            nums[zero_index], nums[curr_index] = nums[curr_index], nums[zero_index]
            zero_index += 1
        print("\t\t", nums)
    print(nums)


print(shift_zeros_to_the_end([0, 1, 0, 3, 2]))
"""

"""
i = 1;
    [0, 1, 0, 3, 2]
        [1, 0, 0, 3, 2]
i = 2;
    [1, 0, 0, 3, 2]
        [1, 0, 0, 3, 2]
i = 3;
    [1, 0, 0, 3, 2]
        [1, 0, 3, 0, 2]
"""

from typing import List


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    seen = {}  # Dictionary to store seen numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
        print("i:", i,"\n", target, "-", num, "=", complement)
        if complement in seen:
            print("\t", seen)
            return [seen[complement], i]
        seen[num] = i

    return []  # No pair found


print(pair_sum_unsorted(nums=[-1, 3, 4, 2], target=3))
