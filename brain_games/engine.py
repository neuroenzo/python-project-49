from typing import Callable

import prompt


GAME_ROUNDS = 3


def launch_game(game: Callable[[], tuple], description: str):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(description)

    for i in range(GAME_ROUNDS):
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
