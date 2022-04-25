"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time 


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers
    :return: int - the time to prepare multiplied by it's layers.

    The number in minutes for the total of layers in the lasagna
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - the number of layers.
    :param elapsed_bake_time: int - the time elapsed of bake time.
    :return: int - the elapsed time in minutes

    Return the elapsed time in minutes of the baking
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)

    return elapsed_bake_time + preparation_time