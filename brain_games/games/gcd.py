import random

GCD_GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def prepare_gcd_game() -> str:
    print(GCD_GAME_DESCRIPTION)
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Question:', f'{number1} {number2}')
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return str(number1 + number2)
