import numpy as np


def score_game(game_logic, times):
    count_ls = []

    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=times)

    for number in random_array:
        count_ls.append(game_logic(number))

    score = int(np.mean(count_ls))

    return score