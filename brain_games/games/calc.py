import random

DESCRIPTION = 'What is the result of the expression?'


def calculate_random_values(number1: int,
                            number2: int,
                            operation: str) -> str:
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)


def get_question_and_answer() -> tuple:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    question = f'{number1} {operation} {number2}'
    answer = calculate_random_values(number1, number2, operation)

    return question, answer
