from argparse import ArgumentParser


def run():
    parser = ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest="command", required=True)

    args = parser.parse_args()


if __name__ == "__main__":
    run()
