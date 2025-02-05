def solution(images):
    """
    I = render independently
    P1 = render in pair as the first item
    P2 = render in pair as the second item
    """
    r = []
    for i, image in enumerate(images):
        if (i + 1) % 3 == 0:
            r.append((image, 'P2'))
        elif (i + 2) % 3 == 0:
            r.append((image, 'P1'))
        else:
            r.append((image, 'I'))
    return r


def reposition_zeros(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == 0 and nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            r += 1
            l += 1
        elif nums[l] == 0 and nums[r] == 0:
            r += 1
        else:
            l += 1
    return nums
    # l, r = 0, len(nums) - 1
    # while l < r:
    #     if nums[l] == 0 and nums[r] != 0:
    #         nums[r], nums[l] = nums[l], nums[r]
    #         r -= 1
    #         l += 1
    #     elif  nums[l] == 0 and nums[r] == 0:
    #         r -= 1
    #     else:
    #         l += 1
    # return nums


def move_zeros(nums):
    n = 0
    last_index = len(nums) - 1
    while last_index > 0:
        for i in range(last_index):
            n += 1
            if nums[i] == 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        last_index -= 1
    print(n, ":", len(nums))
    return nums
