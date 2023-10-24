import random

GAME_DESCRIPTION = 'What number is missing in the progression?'


def prepare_game() -> str:
    start_number = random.randint(1, 100)
    step = random.randint(2, 9)
    dots = '..'
    progression = []
    count = 0
    while count < 10:
        start_number += step
        progression.append(start_number)

        count += 1

    missing_number = progression[step]
    progression[step] = dots
    new_line = " ".join(map(str, progression))
    print(str('Question: 'f'{new_line}'))

    return str(missing_number)
