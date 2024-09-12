from jinja2 import Template as T

class Template:
    TYPE = "proof validation"

    DOMAINS = [
        "basic math",
        "grammar",
        "spelling"
    ]

    SYSTEM_PROMPTS = {
        "validation": "You are an expert {{ system_type }} system that identifies the domain and context for {{ task }} of prompt and response pairs in {{ lang }}."
    }
    
    INSTRUCTIONS = (
        "You are an expert {{ system_type }} system.\n"
        "Your task is to identify the domain, context, and is_valid of the given pair of prompt and response strings.\n"
        "Return the domain, context, and is_valid as plain text.\n"
        "Do not provide any explanations, markdown, code, or other content beside a JSON Object.\n"
        "Only return the domain and context of input prompt and response pair.\n"
        "Return JSON Object of type { \"domain\": domain, \"context\": context, \"is_valid\": is_valid, \"reason\": reason }\n"
        "The domain to choose from are: {{ domains }}.\n"
        "Context is derived from the input prompt-response pair within selected domains and is always non-null.\n"
        "The reason is provided as the what fail the proof of A -> B = A*"
    )

    PROMPT = (
        "System: {{ system }}\n"
        "Instructions: {{ instructions }}\n"
        "Example: {{ example }}\n"
        "User: {{ prompt }}\n"
        "Response: {{ response }}\n"
        "System: Return only the domain and context. No explanations, only the domain and context; e.g., {\"domain\": domain, \"context\": context, \"is_valid\": is_valid, \"reason\": reason}\n"
    )

    TEMPLATES = {
        "validation": T(PROMPT)
    }

    TASKS = {
        "proofs": "Given prompt 'What is 2 + 2?' and response '4' returns domain as 'basic math', context as 'arithmetic', and reason as null"
    }
