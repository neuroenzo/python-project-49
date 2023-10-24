from typing import Callable

import prompt

from brain_games.cli import welcome_user


def launch_game(game: Callable[[], str]):
    user_name = welcome_user()

    for i in range(3):
        correct_answer = game()
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            return False

    print(f'Congratulations, {user_name}!')
