from decimal import Decimal as D


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
    x, y = 0, 1
    while y < len(nums):
        if nums[x] == 0 and nums[y] != 0:
            nums[y], nums[x] = nums[x], nums[y]
            y += 1
            x += 1
        elif nums[x] == 0 and nums[y] == 0:
            y += 1
        else:
            x += 1
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
    last_index = len(nums) - 1
    while last_index > 0:
        for i in range(last_index):
            if nums[i] == 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        last_index -= 1
    return nums


def get_triangle_type(length1, length2, length3):
    """
    Try this. I want to your implementation

    Given three side lengths, determine whether the triangle is:
    Equilateral (all sides equal)
    Isosceles (two sides equal)
    Scalene (all sides different)
    Impossible (violates the triangle inequality theorem)
    """
    if length1 <= 0 or length2 <= 0 or length3 <= 0:
        return "Impossible"

    set_length = len({length1, length2, length3})
    return {
        3: "Scalene",
        2: "Isosceles",
        1: "Equilateral",
    }[set_length]


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def calculate_discount(amount, is_member: bool):
    """
    A store give the following discounts:
    If the purchase amount is above $100, apply a 10% discount.
    If the user is a member, apply an additional 5% discount.
    If the total after discount is above $200, apply another 5% discount.
    Write a method that calculates the final amount.
    """
    def ratio(percent):
        return (100 - percent) / 100

    discounted_price = amount
    if discounted_price > 100:
        discounted_price *= ratio(percent=10)

    if is_member:
        discounted_price *=  ratio(percent=5)

    if discounted_price > 200:
        discounted_price *=  ratio(percent=5)

    return D(discounted_price).quantize(D("0.01"))


def split(data: str, sep=None, maxsplit=-1):
    if sep == '':
        raise ValueError("empty separator")

    size = len(data)
    delimiter = sep or ' '
    del_size = len(delimiter)
    i = del_size
    s = 0
    res = []

    while i <= size and (maxsplit == -1 or len(res) < maxsplit):
        if data[i - del_size: i] == delimiter:
            d = data[s:i - del_size]
            if d != '' or sep is not None:
                res.append(d)
            s = i
        i += 1

    if s != size or sep is not None:
        res.append(data[s:size])
    return res


def replace_char_with_position(string):
    """
    You are required to, given a string, replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.

    "a" = 1, "b" = 2, etc.

    Example

    Input = "The sunset sets at twelve o' clock."
    Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    """
    store = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }
    res = []
    for c in string:
        pos = store.get(c.upper())
        if pos is not None:
            res.append(str(pos))
    return ' '.join(res)


def count_smileys(smiles):
    """
    Given an array (arr) as an argument complete the function count_smileys that should
    return the total number of smiling faces.

    Rules for a smiling face:

    - Each smiley face MUST contain a valid pair of eyes. Eyes can be marked as ':' or ';'.
    - A smiley face can have a nose, but it does not have to. Valid characters for a nose
     are '-' or '~'.
    - Every smiling face MUST have a smiling mouth that should be marked with either ')' or 'D'.
    - No additional characters are allowed except for those mentioned.

    Valid smiley face examples: :) :D ;-D :~)
    Invalid smiley faces:  ;( :> :} :]

    Example

    count_smileys([':)', ';(', ';}', ':-D']);       // should return 2;
    count_smileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
    count_smileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
    Note

    In case of an empty array return 0. You will not be tested with invalid input (input will
    always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
    """
    eyes = {";", ":"}
    noses = {"-", "~"}
    smiling_mouths = {")", "D"}
    valid_smily_characters = eyes | noses | smiling_mouths

    count = 0

    for smily in smiles:
        if len(set(smily) - valid_smily_characters) == 0:
            count += 1

    return count


class TestMeta(type):

    def __new__(cls, name, bases, attrs):
        """Creates the class object."""
        attrs['instance_count_meta'] = 0  # Initialize instance count
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class

    def __call__(cls, *args, **kwargs):
        """Called when a new instance is created."""
        instance = super().__call__(*args, **kwargs)
        # noinspection PyUnresolvedReferences
        cls.instance_count_meta += 1  # Increment the count
        return instance


class Test(metaclass=TestMeta):
    instance_count = 0

    def __init__(self):
        self.__class__.instance_count += 1
