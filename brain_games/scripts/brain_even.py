from brain_games.engine import launch_game
from brain_games.games.even import prepare_even_game


def main():
    launch_game(prepare_even_game)


if __name__ == "__main__":
    main()
