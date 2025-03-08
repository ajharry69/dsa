from decimal import Decimal as D


class CountInstanceMeta(type):

    def __new__(cls, name, bases, attrs):
        """Creates the class object."""
        attrs["instance_count_meta"] = 0  # Initialize instance count
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class

    def __call__(cls, *args, **kwargs):
        """Called when a new instance is created."""
        instance = super().__call__(*args, **kwargs)
        # noinspection PyUnresolvedReferences
        cls.instance_count_meta += 1  # Increment the count
        return instance


class CountInstance(metaclass=CountInstanceMeta):
    instance_count = 0

    def __init__(self):
        self.__class__.instance_count += 1


def solution(images):
    """
    I = render independently
    P1 = render in pair as the first item
    P2 = render in pair as the second item
    """
    r = []
    for i, image in enumerate(images):
        if (i + 1) % 3 == 0:
            r.append((image, "P2"))
        elif (i + 2) % 3 == 0:
            r.append((image, "P1"))
        else:
            r.append((image, "I"))
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
        discounted_price *= ratio(percent=5)

    if discounted_price > 200:
        discounted_price *= ratio(percent=5)

    return D(discounted_price).quantize(D("0.01"))


def split(data: str, sep=None, maxsplit=-1):
    if sep == "":
        raise ValueError("empty separator")

    size = len(data)
    delimiter = sep or " "
    del_size = len(delimiter)
    i = del_size
    s = 0
    res = []

    while i <= size and (maxsplit == -1 or len(res) < maxsplit):
        if data[i - del_size : i] == delimiter:
            d = data[s : i - del_size]
            if d != "" or sep is not None:
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
    char_positions = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    res = []
    for c in string:
        pos = char_positions.get(c.upper())
        if pos is not None:
            res.append(str(pos))
    return " ".join(res)


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


def highest_scoring_word(words: str):
    """
    Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet:
    a = 1, b = 2, c = 3 etc.
    For example, the score of abad is 8 (1 + 2 + 1 + 4).
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string.
    All letters will be lowercase and all inputs will be valid.
    """
    char_positions = {chr(c): i + 1 for i, c in enumerate(range(ord("A"), ord("Z") + 1))}
    highest_score = 0
    highest_scoring = ""

    for word in words.split():
        score = 0
        for c in word:
            score += char_positions[c.upper()]

        if score > highest_score:
            highest_scoring = word
            highest_score = score
    return highest_scoring


def highest_scoring_word_1(words: str):
    """
    Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet:
    a = 1, b = 2, c = 3 etc.
    For example, the score of abad is 8 (1 + 2 + 1 + 4).
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string.
    All letters will be lowercase and all inputs will be valid.
    """
    char_positions = {chr(c): i + 1 for i, c in enumerate(range(ord("A"), ord("Z") + 1))}
    highest_score = 0
    highest_scoring = ""

    current_word_score = 0
    current_word_start_index = 0
    index = 0
    last_index = len(words) - 1

    for c in words:
        if c == " ":
            if current_word_score > highest_score:
                highest_score = current_word_score
                highest_scoring = words[current_word_start_index:index]
            current_word_start_index = index + 1
            current_word_score = 0
        else:
            current_word_score += char_positions[c.upper()]
            if index == last_index and current_word_score > highest_score:
                highest_scoring = words[current_word_start_index : index + 1]
        index += 1

    return highest_scoring


def delete_nth_while_retaining_position(nums: list[int], max_appearances: int):
    """
    SUMMARY

    Delete occurrences of an element if it occurs more than n times

    Enough is enough!
    Alice and Bob were on a holiday. Both of them took many pictures of the places they've been
    and now they want to show Charlie their entire collection.
    However, Charlie doesn't like these sessions, since the motif usually repeats.
    He isn't fond of seeing the Eiffel tower 40 times.
    He tells them that he will only sit for the session if they show the same motif at most N times.
    Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers
    such that their list contains each number only up to N times, without changing the order?

    Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
    For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
    drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
    and then take 3, which leads to [1,2,3,1,2,3].
    With list [20,37,20,21] and number 1, the result would be [20,37,21].
    """
    response = []
    num_count = {}
    for n in nums:
        count = num_count.get(n, 0) + 1
        num_count[n] = count
        if count <= max_appearances:
            response.append(n)

    return response


def first_non_repeating_letter(string: str):
    """
    Write a function named first_non_repeating_letter that takes a string input,
    and returns the first character that is not repeated anywhere in the string.
    For example, if given the input 'stress', the function should return 't', since
    the letter t only occurs once in the string, and occurs first in the string.
    As an added challenge, upper- and lowercase letters are considered the same character,
    but the function should return the correct case for the initial letter.
    For example, the input 'sTreSS' should return 'T'.
    If a string contains all repeating characters, it should return an empty string ("");
    Note: the function is called firstNonRepeatingLetter for historical reasons,
    but your function should handle any Unicode character.
    """
    c_count = {}

    for c in string:
        c = c.lower()
        c_count[c] = c_count.get(c, 0) + 1

    for c in string:
        if c_count[c.lower()] == 1:
            return c

    return ""
