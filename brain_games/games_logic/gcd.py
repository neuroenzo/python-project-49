import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def prepare_game() -> str:
    number1: int = random.randint(1, 100)
    number2: int = random.randint(1, 100)
    print('Question:', f'{number1} {number2}')
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return str(number1 + number2)
