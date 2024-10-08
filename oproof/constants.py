class Const:
    OFFSET_DEFAULT = 1
    RETRIES_DEFAULT = 5
    DEBUG_DEFAULT = False
    MODEL_DEFAULT = 'llama3.1'
    LANG_DEFAULT = 'English'
    ERROR_KEY = 'error'
    ERROR_MESSAGE = 'Error in results'
    ORIGINAL_TEXT_KEY = 'original_text'
    RESPONSES_KEY = 'responses'
    PROOFS_KEY = 'proofs'
    PROMPTS_KEY = 'prompts'
    RUN_COMMAND_ERROR = "Ollama not installed. Install it before running this script."
    PULL_COMMAND_ERROR = "Failed to pull model"
    PROMPT_SEPARATOR = '-' * 100
    STARTING_MAIN_FUNCTION = "Starting main function"
    VALIDATION_ERROR = "Validation error: "
    ERROR_PROCESSING_INPUT = "Error processing input: "
    ARG_TEXT = "text"
    ARG_TEXT_HELP = "Input text"
    ARG_DEBUG = "--debug"
    ARG_DEBUG_HELP = "Enable debug logging"
    ARG_RAW = "--raw"
    ARG_RAW_HELP = "Include raw response in the output JSON"
    ARG_DESCRIPTION = "Oproof script"
    ARG_PROMPT_TEXT = "prompt"
    ARG_PROMPT_TEXT_HELP = "Input prompt"
    ARG_RESPONSE_TEXT = "response"
    ARG_RESPONSE_TEXT_HELP = "Input response"
