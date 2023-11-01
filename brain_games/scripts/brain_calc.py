from brain_games.engine import launch_game
from brain_games.games.calc import get_question_and_answer, DESCRIPTION


def main():
    launch_game(get_question_and_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
