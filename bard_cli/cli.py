"""CLI class to handle stdin/stdout and command line arguments."""

import argparse
import importlib.metadata
import sys

from .utils import color_print


class CLI:
    """CLI class to handle stdin/stdout and command line arguments. also have some functions to handle the commands.
    with argparse to handle the command line arguments.
    """

    def __init__(self):
        """Initiate the CLI class with the parser and the arguments."""
        self.parser = argparse.ArgumentParser(
            description="Bard CLI - Ask me a question and I'll answer you."
        )
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(
                version=importlib.metadata.version("bard_cli")
            ),
        )
        self.parser.add_argument(
            "-p",
            "--prompt",
            metavar="prompt",
            type=str,
            nargs="?",
            help="Prompt for Bard.",
        )
        self.parser.add_argument(
            "-i",
            "--system",
            action="store_true",
            help="Include system info in the question.",
        )
        self.parser.add_argument(
            "-c",
            "--cwd",
            action="store_true",
            help="Include current working directory in the question.",
        )
        self.parser.add_argument(
            "-s",
            "--show",
            action="store_true",
            help="Show the final prompt before sending it.",
        )
        self.parser.add_argument(
            "-t",
            "--cwd-tree",
            action="store_true",
            help="Include current working directory tree in the question.",
        )

    def get_args(self):
        """Get the arguments from the command line and return it as a string."""
        return self.parser.parse_args()

    def get_stdin(self):
        """Get stdin from the from any terminla command piped to bard-cli."""

        # check if stdin is provided
        if not sys.stdin.isatty():
            stdin = sys.stdin.read()
        else:
            stdin = ""

        return stdin

    def print_error(self, error):
        """Print the error to stderr."""
        color_print(error, color="red", file=sys.stderr)

    def print_help(self):
        """Print the help to stdout."""
        color_print(self.parser.format_help(), color="yellow")

    def print_answer(self, answer: str):
        """Print the answer to stdout."""
        color_print(f"Answer:\n{answer}", color="green")

    def print_prompt(self, prompt: str):
        """Print the prompt to stdout."""
        color_print(f"Prompt:\n{prompt}", color="blue", attrs=["bold"])
