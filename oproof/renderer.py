from jinja2 import Template as T
from .template import Template
from .constants import Const

class Renderer:
    @staticmethod
    def render_prompt(prompt: str, response: str, system_prompt: str, instructions: str, cfg) -> str:
        task_name = list(Template.TASKS.keys())[0]
        rendered_template = Template.TEMPLATES["validation"].render(
            system=system_prompt,
            task=task_name,
            text=prompt,
            example=Template.TASKS[task_name],
            instructions=instructions,
            lang=cfg.lang,
            prompt=prompt,
            response=response
        )
        return Renderer._post_process(rendered_template)

    @staticmethod
    def _post_process(prompt: str) -> str:
        task_name = list(Template.TASKS.keys())[0]
        replacements = {
            "{{ task }}": task_name,
            "{{ lang }}": Const.LANG_DEFAULT,
            "{{ system_type }}": Template.SYSTEM_TYPE,
            "{{ domains }}": ', '.join(Template.DOMAINS)
        }
        for key, value in replacements.items():
            prompt = prompt.replace(key, value)
        return prompt
