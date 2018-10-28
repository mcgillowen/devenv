"""
Main file for the command line configuration.

Sets up the ArgumentParser
"""
import argparse
import sys

config = {"tool": {"poetry": {"name": sys.argv[0], "description": "DevEnv"}}}


def main_cmd(parser: argparse.ArgumentParser):
    """
    Set up main command for DevEnv.

    :param parser: the initialised ArgumentParser
    """
    pass


def setup_arguments(config: dict = config):
    """
    Set up all the program commands.

    :param config: the dict from the pyproject.toml
    :returns: the configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog=config["tool"]["poetry"]["name"],
        description=config["tool"]["poetry"]["description"],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    return parser


if __name__ == "__main__":
    setup_arguments()
