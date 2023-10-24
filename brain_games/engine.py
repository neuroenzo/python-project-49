from typing import Callable

import prompt

from brain_games.cli import welcome_user


def launch_game(game_description: str, prepare_game: Callable[[], str]):
    user_name = welcome_user()
    print(game_description)

    for i in range(3):
        answer = prepare_game()
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            return False

    print(f'Congratulations, {user_name}!')
