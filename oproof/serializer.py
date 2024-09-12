from typing import List, Dict, Any

class Serializer:
    @staticmethod
    def serialize_output(text: str, responses: List[Dict[str, Any]], include_raw: bool) -> Dict[str, Any]:
        result = {
            "original_text": text,
            "responses": [
                Serializer._serialize_response(response, include_raw)
                for response in responses
            ]
        }
        return result

    @staticmethod
    def _serialize_response(response: Dict[str, Any], include_raw: bool) -> Dict[str, Any]:
        serialized_response = {
            "prompt": response.get("prompt", ""),
            "response": response.get("response", ""),
            "is_valid": response.get("is_valid", False),
            "domain": response.get("domain", "unknown"),
            "context": response.get("context", "unknown")
        }
        
        if not response.get("is_valid", False) and response.get("reason") is not None:
            serialized_response["reason"] = response.get("reason")
        
        if include_raw and response.get("raw_response") is not None:
            serialized_response["raw_response"] = response.get("raw_response")
        
        return serialized_response
