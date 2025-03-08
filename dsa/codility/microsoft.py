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

    return len(ra + rb)


def reverse_polish_notation(tokens):
    """
    You are given an array of string tokens that represent an
    arithmetic expression in Reverse Polish Notation.
    For example, "2 3 +" means "2 + 3"

    Return an integer that represents the value of the expression.

    Intuition:

    Use a stack to record intermediate results.

    Pop off the 2 most recent results when an operator appears.

    Append result to stack.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    ops = {"+": 0, "-": 1, "*": 2, "/": 3}

    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            a, b = stack.pop(), stack.pop()
            result = [a + b, a - b, a * b, a / b][ops[token]]
            stack.append(result)

    return stack[0]
