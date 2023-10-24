from brain_games.engine import launch_game
from brain_games.games.prime import prepare_prime_game


def main():
    launch_game(prepare_prime_game)


if __name__ == "__main__":
    main()
