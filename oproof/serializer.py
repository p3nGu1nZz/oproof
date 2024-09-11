from typing import List, Dict, Any

class Serializer:
    @staticmethod
    def serialize_output(text: str, responses: List[Dict[str, Any]], response_prompts: List[str], include_prompts: bool) -> Dict[str, Any]:
        result = {
            "original_text": text,
            "responses": [
                {
                    "prompt": response["prompt"],
                    "response": response["response"],
                    "is_valid": response["is_valid"],
                    "domain": response.get("domain", "unknown"),
                    "context": response.get("context", "unknown"),
                    "reason": response.get("reason", None)
                }
                for response in responses
            ]
        }
        if include_prompts:
            result["prompts"] = response_prompts
        return result
