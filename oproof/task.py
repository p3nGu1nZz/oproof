import subprocess
from typing import List, Dict, Any
from .constants import Const
from .template import Template
from .log import Log
from .renderer import Renderer
from .response import Response
import ollama as oll
from httpx import ConnectError

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
        rendered_prompt = Renderer.render_prompt(prompt, response, system_prompt, instructions, self.cfg)
        Log.debug(f"Prompt: {rendered_prompt}")
        
        output = self._generate_output(rendered_prompt)
        Log.debug(f"Response: {output}")
        Log.debug(Const.PROMPT_SEPARATOR)
        
        if Const.ERROR_KEY in output:
            raise Exception(output[Const.ERROR_KEY])
       
        response_obj = Response(prompt, response, rendered_prompt, output)
        return response_obj.get_response_data()

    def _log_error_and_raise(self, error_message: str, exception_message: str) -> None:
        Log.error(error_message)
        raise Exception(exception_message)

    def _generate_output(self, prompt: str) -> Dict[str, Any]:
        try:
            return oll.generate(prompt=prompt, model=self.cfg.model)
        except ConnectError:
            with Log.suppress_logs():
                error_message = "Ollama is not running or installed. Please ensure Ollama is running and try again."
                return {Const.ERROR_KEY: error_message}
