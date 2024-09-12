from typing import List, Dict, Any

class Serializer:
    @staticmethod
    def serialize_output(text: str, responses: List[Dict[str, Any]], response_prompts: List[Dict[str, str]], include_prompts: bool) -> Dict[str, Any]:
        result = {
            "original_text": text,
            "responses": [
                {
                    "prompt": response.get("prompt", ""),
                    "response": response.get("response", ""),
                    "is_valid": response.get("is_valid", False),
                    "domain": response.get("domain", "unknown"),
                    "context": response.get("context", "unknown"),
                    "reason": response.get("reason", "No reason provided"),
                    "raw_response": response.get("raw_response", "")  # Include the raw response
                }
                for response in responses
            ]
        }
        if include_prompts:
            result["prompts"] = response_prompts
        return result
