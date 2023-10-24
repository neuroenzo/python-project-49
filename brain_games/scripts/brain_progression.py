from brain_games.engine import launch_game
from brain_games.games.progression import GAME_DESCRIPTION, prepare_game


def main():
    launch_game(GAME_DESCRIPTION, prepare_game)


if __name__ == "__main__":
    main()
