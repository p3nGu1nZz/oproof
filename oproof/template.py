from jinja2 import Template as T

class Template:
    SYSTEM_TYPE = "proof validation"

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
        "Return the domain, context, is_valid as plain text.\n"
        "Do not provide any explanations, markdown, code, or other content beside a JSON Object.\n"
        "Only return the domain and context of input prompt and response pair.\n"
        "Return JSON Object of type { \"domain\": domain, \"context\": context, \"is_valid\" }\n"
        "The domain to choose from are: {{ domains }}.\n"
        "The context is extrapolated from input prompt and response pair based in selected domains.\n"
        ""
    )

    PROMPT = (
        "System: {{ system }}\n"
        "Instructions: {{ instructions }}\n"
        "Example: {{ example }}\n"
        "User: {{ prompt }}\n"
        "Response: {{ response }}\n"
        "System: Return only the domain and context. No explanations, only the domain and context; e.g., {\"domain\": \"basic math\", \"context\": \"arithmetic\"}\n"
    )

    TEMPLATES = {
        "validation": T(PROMPT)
    }

    TASKS = {
        "proofs": "Given prompt 'What is 2 + 2?' and response '4' returns 'basic math' with context 'arithmetic'"
    }
