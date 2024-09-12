from typing import List, Dict, Any
from .log import Log
from .constants import Const
from .template import Template
from .error import ValidationError

class Validator:
    def __init__(self, cfg, task):
        self.cfg = cfg
        self.task = task

    def validate(self, prompt: str, response: str) -> Dict[str, Any]:
        Log.debug(f"Validating response for prompt: {prompt}")
        result = self._collect_validation(prompt, response)
        Log.debug(f"Collected validation result: {result}")
        
        return result

    def _collect_validation(self, prompt: str, response: str) -> Dict[str, Any]:
        validation_template = Template.TEMPLATES["validation"]
        system_prompt = Template.SYSTEM_PROMPTS["validation"]
        validation_result = self.task.execute(prompt, response, validation_template, system_prompt, Template.INSTRUCTIONS)
        
        if Const.ERROR_KEY in validation_result:
            Log.error(f"Validation error: {validation_result[Const.ERROR_KEY]}")
            raise ValidationError(validation_result[Const.ERROR_KEY])
        
        # Ensure required keys are present
        is_valid = validation_result.get('is_valid', False)
        domain = validation_result.get('domain', 'unknown')
        context = validation_result.get('context', 'unknown')
        reason = validation_result.get('reason', 'No reason provided')
        
        return {
            'is_valid': is_valid,
            'domain': domain,
            'context': context,
            'reason': reason,
            'raw_response': validation_result  # Include the raw response
        }
