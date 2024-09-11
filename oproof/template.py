from jinja2 import Template as T

class Template:
    INSTRUCTIONS = (
        "Provide the task as plain JSON, no explanations or markdown.\n"
        "Return a JSON object with the validation result.\n"
        "The object should include 'is_valid', 'domain', 'context', and 'reason' fields.\n"
        "No markdown or code.\n"
        "Do not answer the input; only validate the response.\n"
        "No explanations; only the JSON object."
    )

    SYSTEM_PROMPTS = {
        "validation": "You are an expert validation system that validates responses for {{ task }}s. Validate the following response in {{ lang }}."
    }

    PROMPT_TEMPLATE = (
        "System: {{ system }}\n"
        "Instructions: {{ instructions }}\n"
        "Example: {{ example }}\n"
        "User: {{ prompt }}\n"
        "Response: {{ response }}\n"
        "System: Return only a JSON object with the validation result. No explanations, only JSON object; eg. {\"is_valid\": true, \"domain\": \"basic math\", \"context\": \"arithmetic\", \"reason\": null}"
    )

    TEMPLATES = {
        "validation": T(PROMPT_TEMPLATE)
    }

    TASKS = {
        "validate": "Validate the response for the given prompt."
    }
