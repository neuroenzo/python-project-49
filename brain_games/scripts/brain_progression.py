from brain_games.engine import launch_game
from brain_games.games.progression import prepare_progression_game


def main():
    launch_game(prepare_progression_game)


if __name__ == "__main__":
    main()
