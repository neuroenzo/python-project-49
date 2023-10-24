import random

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prepare_game() -> str | None:
    number = random.randint(1, 100)
    print(str('Question: 'f'{number}'))

    if number <= 1:
        return

    divider = 2
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            divider += 1

    if divider > 2:
        return 'no'
    else:
        return 'yes'
