import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Finds a route for pawn destroying."
    )
    parser.add_argument(
        "input_filename", type=str, nargs="+", help="path to file contains input data"
    )
    return parser.parse_args()
