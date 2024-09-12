from typing import List, Dict, Any
from .task import Task
from .validator import Validator
from .log import Log
from .constants import Const
from .config import Config
from .template import Template

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
        
        domain = validation_result.get('domain', 'unknown')
        context = validation_result.get('context', 'unknown')
        
        return {
            'prompt': prompt,
            'response': response,
            'is_valid': validation_result['is_valid'],
            'domain': domain,
            'context': context,
            'reason': validation_result.get('reason', None),
            'raw_response': validation_result.get('raw_response', "")
        }

    def generate_prompt(self, prompt: str, response: str) -> str:
        return self.task._render_prompt(prompt, response, Template.TEMPLATES["validation"], Template.SYSTEM_PROMPTS["validation"], Template.INSTRUCTIONS)
