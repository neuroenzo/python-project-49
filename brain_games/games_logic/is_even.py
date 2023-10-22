import random
import prompt

from brain_games.cli import welcome_user


def is_even_number():
    random_number = random.randint(1, 100)
    even_number = 'yes' if random_number % 2 == 0 else 'no'
    return even_number, random_number


def launch_game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        answer, random_number = is_even_number()

        print(str('Question: 'f'{random_number}'))
        user_answer = prompt.string('Your answer: ')

        if answer == user_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{answer}\'.')

            print(f'Let\'s try again, {user_name}!')
            return False

    print(f'Congratulations, {user_name}!')
