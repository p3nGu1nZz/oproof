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
        "Your task is to identify the domain and context of the given pair of prompt and response strings.\n"
        "Return the domain and context as plain text.\n"
        "Do not provide any explanations, markdown, code, or other content beside a JSON Object.\n"
        "Only return the domain and context of input prompt and response pair.\n"
        "Return JSON Object of type { \"domain\": domain, \"context\": context }\n"
        "The domains to choose from are: {{ domains }}."
        "Infer the context based from input prompt and response pair in extrapolated domains"
    )

    PROMPT = (
        "System: {{ system }}\n"
        "Instructions: {{ instructions }}\n"
        "Example: 'What is 2 + 2?' '4' returns 'basic math' with context 'arithmetic'\n"
        "User: {{ prompt }}\n"
        "Response: {{ response }}\n"
        "System: Return only the domain and context. No explanations, only the domain and context; e.g., {\"domain\": \"basic math\", \"context\": \"arithmetic\"}\n"
    )

    TEMPLATES = {
        "validation": T(PROMPT)
    }

    TASKS = {
        "proofs": "Proof the given prompt and response pair of input text strings. e.g., 'What is 2 + 2?' '4' returns 'basic math' with context 'arithmetic'\n"
    }
