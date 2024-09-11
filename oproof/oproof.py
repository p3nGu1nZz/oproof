import json
from typing import List, Dict, Any, Tuple
from .constants import Const
from .config import Config
from .manager import Manager

class Oproof:
    def __init__(self, cfg: Config):
        self.manager = Manager(cfg)

    def check(self) -> None:
        self.manager.check()

    def pull(self) -> None:
        self.manager.pull()

    def validate(self, prompt: str, response: str) -> Dict[str, Any]:
        return self.manager.validate(prompt, response)
