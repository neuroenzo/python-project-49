from brain_games.engine import launch_game
from brain_games.games_logic.calc import describe_game, prepare_game


def main():
    launch_game(describe_game, prepare_game)


if __name__ == "__main__":
    main()
