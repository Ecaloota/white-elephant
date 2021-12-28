import argparse


def user_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="make verbose", default=False
    )
    parser.add_argument(
        "-u",
        "--unbiased",
        action="store_false",
        help="whether npc choices are biased by gift values. if False, results are biased",
        default=True,
    )
    parser.add_argument(
        "-r",
        "--rounds",
        "--games",
        type=int,
        help="the number of games to play",
        default=100,
    )
    parser.add_argument(
        "-n", "--players", type=int, help="the number of players per game", default=10
    )

    parser.add_argument(
        "-w",
        "--write",
        "--output",
        help="to write outputs or not",
        default=True,
    )

    parser.add_argument(
        "-p",
        "--plot",
        help="to write plots or not",
        default=True,
    )

    args = parser.parse_args()

    if args.players <= 1:
        raise ValueError("Number of players must be greater than 1.")
    elif args.rounds < 1:
        raise ValueError("Number of rounds must be greater than 1")

    return args
