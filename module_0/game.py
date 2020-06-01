import math


def guess(number):
    """Function accepts a number and tries to guess it using as less attempts as possible.
    It is using divide and conquer logic, so it tries to find the range where the number is
    and ignores other ranges.

    Args:
        number (int): A number to guess

    Returns:
        int: Number of attempts used to guess the number
    """

    count = 1

    low = 1
    high = 100

    predict = high / 2  # first prediction is half of the highest possible number

    while number != predict and number != low and number != high:
        count += 1

        if number > predict:  # if number is higher than prediction, then we can ignore lower numbers
            low = predict
        elif number < predict:  # if number is lower than prediction, then we can ignore higher numbers
            high = predict

        predict = math.floor((high + low) / 2)  # divide range between low and high to get new prediction

    return count
