from typing import List, Dict, Any
from .task import Task
from .validator import Validator
from .log import Log
from .constants import Const
from .config import Config

class Manager:
    def __init__(self, config: Config):
        self.config = config
        self.task = Task(config)
        self.validator = Validator(config, self.task)
        self.log = Log

    def check_version(self) -> None:
        self.task.run(['ollama', '--version'], Const.RUN_COMMAND_ERROR)

    def pull_model(self) -> None:
        self.task.run(['ollama', 'pull', self.config.model], f"{Const.PULL_COMMAND_ERROR} {self.config.model}.")

    def validate_response(self, prompt: str, response: str) -> Dict[str, Any]:
        validation_result = self.validator.validate(prompt, response)
        
        # Extract domain and context from the validation result
        domain = validation_result.get('domain', 'unknown')
        context = validation_result.get('context', 'unknown')
        
        return {
            'prompt': prompt,
            'response': response,
            'is_valid': validation_result['is_valid'],
            'domain': domain,
            'context': context,
            'reason': validation_result.get('reason', None)
        }
