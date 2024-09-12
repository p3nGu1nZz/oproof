import argparse
from .constants import Const

class Args:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description=Const.ARG_DESCRIPTION)
        self.parser.add_argument(Const.ARG_PROMPT_TEXT, type=str, help=Const.ARG_PROMPT_TEXT_HELP)
        self.parser.add_argument(Const.ARG_RESPONSE_TEXT, type=str, help=Const.ARG_RESPONSE_TEXT_HELP)
        self.parser.add_argument(Const.ARG_DEBUG, action="store_true", help=Const.ARG_DEBUG_HELP)
        self.parser.add_argument(Const.ARG_PROMPT, action="store_true", help=Const.ARG_PROMPT_HELP)
        self.args = None

    def parse(self):
        self.args = self.parser.parse_args()
        return self.args
