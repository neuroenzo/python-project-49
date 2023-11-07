import operator
import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer() -> tuple:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    operation, function = random.choice(operators)

    question = f'{number1} {operation} {number2}'
    answer = str(function(number1, number2))

    return question, answer
