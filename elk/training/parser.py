from argparse import ArgumentParser


def get_training_parser() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument("name", type=str, help="Name of the experiment")
    parser.add_argument(
        "--device",
        type=str,
        help="PyTorch device to use. Default is cuda:0 if available.",
    )
    parser.add_argument(
        "--loss",
        type=str,
        default="squared",
        choices=("js", "squared"),
        help="Loss function used for CCS.",
    )
    parser.add_argument(
        "--optimizer",
        type=str,
        default="lbfgs",
        choices=("adam", "lbfgs"),
        help="Optimizer for CCS. Should be adam or lbfgs.",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--weight-decay",
        type=float,
        default=0.01,
        help=(
            "Weight decay for CCS when using Adam. Used as L2 regularization in LBFGS."
        ),
    )
    return parser