class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        i = self.__hash(key)

        if self.data_map[i] is None:
            self.data_map[i] = [[key, value]]
        else:
            self.data_map[i].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        for _key, value in self.data_map[index] or []:
            if _key == key:
                return value

        return

    def keys(self):
        all_keys = []

        for data in self.data_map:
            if data is None:
                continue

            for key, _ in data:
                all_keys.append(key)

        return all_keys


def item_in_common(list1, list2):
    items = {}

    for item in list1:
        items[item] = True

    for item in list2:
        if items.get(item) is not None:
            return True
        items[item] = True

    return False


def find_duplicates(nums):
    ns = {}

    duplicates = {}

    for num in nums:
        if num in ns:
            duplicates[num] = 1
        else:
            ns[num] = 1
    return list(duplicates.keys())


def find_duplicates_2(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


def first_non_repeating_char(string):
    chars = {}

    for c in string:
        chars[c] = chars.get(c, 0) + 1

    for c, v in chars.items():
        if v == 1:
            return c


def group_anagrams(strings):
    anagrams = {}

    for string in strings:
        k = "".join(sorted(string))
        v = anagrams.get(k, [])
        v.append(string)
        anagrams[k] = v

    return list(anagrams.values())


def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        complement_index = num_map.get(complement)
        if complement_index is not None:
            return [complement_index, i]
        num_map[num] = i

    return []


def subarray_sum(nums, target):
    """
    Given an array of integers `nums` and a `target` integer `target`, write a Python function
    called `subarray_sum` that finds the indices of a contiguous subarray in `nums` that add
    up to the `target` sum using a hash table (dictionary).

    Your function should take two arguments:
        - nums: a list of integers representing the input array
        - target: an integer representing the target sum

    Your function should return a list of two integers representing the starting and ending
    indices of the subarray that adds up to the target sum. If there is no such subarray,
    your function should return an empty list.

    For example:

    ```python
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(subarray_sum(nums, target))  # should print [1, 3]
    ```

    Note that there may be multiple subarrays that add up to the target sum, but your function
    only needs to return the indices of any one such subarray. Also, the input list may contain
    both positive and negative integers.
    """
    current_sum = 0
    # We create a dictionary called 'sum_index' to store
    # running sums (as keys) and their corresponding
    # indices in the array (as values).
    #
    # Why start with {0: -1}?
    # - '0' will serve as the default sum when looking for subarrays.
    # - '-1' indicates there's no subarray yet.
    # This setup helps handle special cases, such as when the
    # first element itself is equal to the target.
    sum_index = {current_sum: -1}

    for i, num in enumerate(nums):
        current_sum += num
        starting_index = sum_index.get(current_sum - target)
        if starting_index is not None:
            return [starting_index + 1, i]

        sum_index[current_sum] = i
    return []


##############################################
# SETS
##############################################
def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True


def has_unique_chars_1(string):
    return len(set(string)) == len(string)
