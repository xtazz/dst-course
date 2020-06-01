import math


def guess(number):
    count = 1

    low = 1
    high = 100

    predict = high / 2

    while number != predict and number != low and number != high:
        count += 1

        if number > predict:
            low = predict
        elif number < predict:
            high = predict

        predict = math.floor((high + low) / 2)

    return count
