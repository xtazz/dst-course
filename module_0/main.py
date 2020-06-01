import numpy as np
from game import guess


def score_game(game_logic, times):
    """Runs game logic for specified number of times to find mean of attempts used to guess the number.

    Args:
        game_logic: Function with game logic
        times (int): Number of times to run the game logic function

    Returns:
        int: Mean attempts used by game logic function
    """

    count_ls = []

    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=times)

    for number in random_array:
        count_ls.append(game_logic(number))

    score = int(np.mean(count_ls))

    return score


attempts = score_game(guess, 1000)
print(f"Provided game logic function guesses the number using on average {attempts} attempts")
