def bubble_sort(my_list):
    """
    The function should perform the following tasks:
        1. Accept a parameter my_list that represents the list of integers to be sorted.
        2. Iterate through the list from the last element to the first element. For each
         element i, perform the following steps:
            1. Iterate through the list from the first element to the element at
            position i - 1. For each element j, perform the following steps:
                - Compare the element at position j with the element at position j + 1.
                 If the element at position j is greater than the element at
                 position j + 1, swap the two elements.

        3. Return the sorted list.
    """
    n = len(my_list)
    while n > 1:
        j = 1

        while j < n:
            if my_list[j - 1] > my_list[j]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j += 1

        n -= 1


def selection_sort(my_list):
    """
    Write a function called selection_sort that sorts a list of integers in ascending
    order using the Selection Sort algorithm.

    The function should perform the following tasks:
        1. Accept a parameter my_list that represents the list of integers to be sorted.
        2. Iterate through the list from the first element to the second-to-last element.
         For each element i, perform the following steps:
            i). Set min_index to the index of the current element i.
            ii). Iterate through the list from the element at position i + 1 to the last
             element. For each element j, perform the following steps:
                - Compare the element at position j with the element at position min_index.
                 If the element at position j is less than the element at position
                 min_index, update min_index to the index j.

            iii). If the index i is not equal to min_index, swap the elements at
            positions i and min_index.

        3. Return the sorted list.
    """
    n = len(my_list)
    i = 0

    while i < n - 1:
        min_index = i
        j = i + 1

        while j < n:
            if my_list[j] < my_list[min_index]:
                min_index = j
            j += 1
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
        i += 1


def insertion_sort(my_list):
    """
    BEST FOR: Almost sorted data
    Write a function called insertion_sort that sorts a list of integers in ascending
     order using the Insertion Sort algorithm.

    The function should perform the following tasks:
        1. Accept a parameter my_list that represents the list of integers to be sorted.
        2. Iterate through the list from the second element to the last element. For
        each element i, perform the following steps:
            i). Store the value of the element at position i in a temporary variable
            called temp.
            ii). Initialize another variable j to i - 1.
            iii). While temp is less than the element at position j and j is greater
            than or equal to 0, perform the following steps:
                - Move the element at position j to the position j + 1.
                - Place the value of temp at position j.
                - Decrement j by 1.
        3. Return the sorted list.
    """

    i = 1
    n = len(my_list)
    while i < n:
        j = i
        while j > 0 and my_list[j] < my_list[j - 1]:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1
        i += 1


def merge(l1, l2):
    result = []

    n1 = len(l1)
    n2 = len(l2)

    i = j = 0
    while i < n1 and j < n2:
        if l1[i] == l2[j]:
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    while i < n1:
        result.append(l1[i])
        i += 1

    while j < n2:
        result.append(l2[j])
        j += 1

    return result


def merge_sort(my_list):
    n = len(my_list)
    if n < 2:
        return my_list
    mid_index = n // 2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(l1=left, l2=right)
