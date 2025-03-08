import math


def get_ratings(rating):
    ratings = ["empty", "empty", "empty", "empty", "empty"]

    rating_as_float = float(rating)
    if rating_as_float <= 0:
        return " ".join(ratings)

    number_of_full_ratings = math.floor(rating_as_float)
    for index in range(0, number_of_full_ratings):
        ratings[index] = "full"

    unclassified_rating = rating_as_float - number_of_full_ratings
    if unclassified_rating <= 0.5:
        ratings[number_of_full_ratings] = "half"
    elif unclassified_rating > 0.5:
        ratings[number_of_full_ratings] = "full"

    return " ".join(ratings)
