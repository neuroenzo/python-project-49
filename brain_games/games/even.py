import random

EVEN_GAME_DESCRIPTION = 'Answer "yes" if the number is even,' \
                        ' otherwise answer "no".'


def prepare_even_game() -> str:
    print(EVEN_GAME_DESCRIPTION)
    random_number = random.randint(1, 100)
    even_number = 'yes' if random_number % 2 == 0 else 'no'
    print(str('Question: 'f'{random_number}'))

    return even_number
