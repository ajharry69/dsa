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
