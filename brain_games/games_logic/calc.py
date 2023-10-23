import random

GAME_DESCRIPTION = 'What is the result of the expression?'


def prepare_game() -> str:
    number1: int = random.randint(1, 100)
    number2: int = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    print('Question:', f'{number1} {operation} {number2}')
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)
