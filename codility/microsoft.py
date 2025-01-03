def solution1(values, K, L):
    values.sort()
    n = len(values)
    for i in range(L, n):
        if values[i] > K or values[i - L] == values[i] - L:
            return False
    return values[n - 1] == K


# def solution1(values, K, L):
#     counts = {}
#     for value in values:
#         counts[value] = counts.get(value, 0) + 1
#         if value > K or counts[value] > L:
#             return False
#     return True

def solution2(A, B):
    left, right = 1, max(A, B)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if (A // mid) + (B // mid) >= 4:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def solution3(A, B):
    gc = int(len(A) / 2)
    sc = int(len(B) / 2)

    ra = list(set(A))[:gc]

    rb = []
    for n in set(B):
        if len(rb) == sc:
            break

        if n not in ra:
            rb.append(n)

    return  len(ra + rb)
