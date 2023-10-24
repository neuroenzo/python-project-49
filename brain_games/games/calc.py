import random

CALC_GAME_DESCRIPTION = 'What is the result of the expression?'


def prepare_calc_game() -> str:
    print(CALC_GAME_DESCRIPTION)
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    print('Question:', f'{number1} {operation} {number2}')
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)
