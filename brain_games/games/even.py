import random

DESCRIPTION = 'Answer "yes" if the number is even,' \
                        ' otherwise answer "no".'


def is_even_number(random_number: int) -> str:
    even_number = 'yes' if random_number % 2 == 0 else 'no'
    return even_number


def get_question_and_answer() -> tuple:
    question = random.randint(1, 100)
    answer = is_even_number(question)

    return question, answer

