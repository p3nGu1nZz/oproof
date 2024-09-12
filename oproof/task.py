import subprocess
import json
from typing import List, Dict, Any
from .constants import Const
from .template import Template
from .log import Log
import ollama as oll
from httpx import ConnectError  # Import the ConnectError exception

class Task:
    def __init__(self, cfg):
        self.cfg = cfg

    def run(self, cmd: List[str], error_msg: str = Const.RUN_COMMAND_ERROR) -> None:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                self._log_error_and_raise(result.stdout, error_msg)
        except FileNotFoundError:
            self._log_error_and_raise(error_msg, error_msg)

    def execute(self, prompt: str, response: str, template, system_prompt, instructions) -> Dict[str, Any]:
        rendered_prompt = self._render_prompt(prompt, response, template, system_prompt, instructions)
        processed_prompt = self._post_process(rendered_prompt)
        Log.debug(f"Prompt: {processed_prompt}")
        
        output = self._generate_output(processed_prompt)
        Log.debug(f"Response: {output}")
        Log.debug(Const.PROMPT_SEPARATOR)
        
        if Const.ERROR_KEY in output:
            raise Exception(output[Const.ERROR_KEY])
       
        parsed_response = self._parse_response(output['response'])
        Log.debug(f"Parsed Response: {parsed_response}")
        
        return {"prompt": processed_prompt, "data": output['response'], "response": parsed_response}

    def _log_error_and_raise(self, error_message: str, exception_message: str) -> None:
        Log.error(error_message)
        raise Exception(exception_message)

    def _render_prompt(self, prompt: str, response: str, template, system_prompt, instructions) -> str:
        return template.render(
            system=system_prompt,
            task="validate",  # Use a valid task name
            text=prompt,
            example=Template.TASKS["validate"],  # Use the corresponding task
            instructions=instructions,
            lang=self.cfg.lang
        )

    def _post_process(self, prompt: str) -> str:
        replacements = {
            "{{ task }}": prompt,
            "{{ lang }}": Const.LANG_DEFAULT
        }
        for key, value in replacements.items():
            prompt = prompt.replace(key, value)
        return prompt

    def _generate_output(self, prompt: str) -> Dict[str, Any]:
        try:
            return oll.generate(prompt=prompt, model=self.cfg.model)
        except ConnectError as e:
            with Log.suppress_logs():
                error_message = "Ollama is not running or installed. Please ensure Ollama is running and try again."
                return {Const.ERROR_KEY: error_message}

    def _parse_response(self, response: str) -> Any:
        Log.debug(f"Raw response: {response}")
        try:
            corrected_response = self._correct_response(response)
            return json.loads(corrected_response)
        except json.JSONDecodeError as e:
            Log.error(f"JSON decode error: {e}")
            return {"error": "Invalid JSON response"}

    def _correct_response(self, response: str) -> str:
        if response.startswith("[") and response.endswith("]"):
            response = "{" + response[1:-1] + "}"
        return response
