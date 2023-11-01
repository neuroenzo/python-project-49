from typing import Callable

import prompt

from brain_games.cli import welcome_user


def launch_game(game: Callable[[], tuple], description: str):
    user_name = welcome_user()

    print(description)

    for round_of_game in range(3):
        question, correct_answer = game()
        print('Question: 'f'{question}')
        user_answer = prompt.string('Your answer: ').lower()
        if correct_answer != user_answer:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            return

        print('Correct')

    print(f'Congratulations, {user_name}!')
