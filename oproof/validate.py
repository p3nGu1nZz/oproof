from typing import List, Dict, Any
from .log import Log
from .validator import Validator

class Validate:
    def __init__(self, cfg, task):
        self.cfg = cfg
        self.task = task
        self.validator = Validator(cfg, task)

    def validate(self, prompt: str, response: str) -> List[Dict[str, Any]]:
        Log.debug(f"Validating response for prompt: {prompt}")
        validation_results = self._collect_validations(prompt, response)
        Log.debug(f"Validation results: {validation_results}")
        return validation_results

    def _collect_validations(self, prompt: str, response: str) -> List[Dict[str, Any]]:
        validation_results = self.validator.validate(prompt, response)
        return validation_results
