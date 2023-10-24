from brain_games.engine import launch_game
from brain_games.games.gcd import prepare_gcd_game


def main():
    launch_game(prepare_gcd_game)


if __name__ == "__main__":
    main()
