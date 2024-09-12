from typing import List, Dict, Any

class Serializer:
    @staticmethod
    def serialize_output(text: str, responses: List[Dict[str, Any]], include_prompts: bool) -> Dict[str, Any]:
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
                    "raw_response": response.get("raw_response", "") if include_prompts else None
                }
                for response in responses
            ]
        }
        return result
