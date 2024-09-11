from typing import NamedTuple

class Prompt(NamedTuple):
    task_type: str
    instructions: str
    system_prompt: str
    template: str
