from brain_games.engine import launch_game
from brain_games.games.calc import prepare_calc_game


def main():
    launch_game(prepare_calc_game)


if __name__ == "__main__":
    main()
