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
        response_data = {
            "prompt": self.prompt,
            "response": self.response,
            "is_valid": self.parsed_response.get("is_valid", False),
            "domain": self.parsed_response.get("domain", "unknown"),
            "context": self.parsed_response.get("context", "unknown")
        }
        
        if not self.parsed_response.get("is_valid", False) and self.parsed_response.get("reason") is not None:
            response_data["reason"] = self.parsed_response.get("reason")
        
        if self.output.get("raw_response") is not None:
            response_data["raw_response"] = {
                "prompt": self.rendered_prompt,
                "data": self.output['response'],
                "response": self.parsed_response
            }
        
        return response_data

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
