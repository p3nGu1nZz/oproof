import json
from typing import Dict, Any
from .log import Log

class Response:
    def __init__(self, prompt: str, response: str, rendered_prompt: str, output: Dict[str, Any]):
        self.prompt = prompt
        self.response = response
        self.rendered_prompt = rendered_prompt
        self.output = output
        self.parsed_response = self._parse_response(output['response'])

    def get_response_data(self) -> Dict[str, Any]:
        return {
            "prompt": self.prompt,
            "response": self.response,
            "is_valid": self.parsed_response.get("is_valid", False),
            "domain": self.parsed_response.get("domain", "basic math"),
            "context": self.parsed_response.get("context", "arithmetic"),
            "reason": self.parsed_response.get("reason", None),
            "raw_response": {
                "prompt": self.rendered_prompt,
                "data": self.output['response'],
                "response": self.parsed_response
            }
        }

    def _parse_response(self, response: str) -> Any:
        Log.debug(f"Raw response: {response}")
        try:
            corrected_response = self._correct_response(response)
            return json.loads(corrected_response)
        except Exception as ex:
            return {"error": str(ex)}

    def _correct_response(self, response: str) -> str:
        if response.startswith("[") and response.endswith("]"):
            response = "{" + response[1:-1] + "}"
        return response
