import json
from rich.console import Console
from rich.panel import Panel
from .constants import Const

console = Console()

class ValidationError(Exception):
    pass

def handle_error(e: Exception, debug: bool) -> None:
    error_output = {Const.ERROR_KEY: f"{Const.ERROR_PROCESSING_INPUT}{e}"}
    if debug:
        import traceback
        error_output["trace"] = traceback.format_exc()
        console.print_exception(show_locals=True)
    else:
        console.print(Panel(f"[red]Error:[/red] {str(e)}", border_style="red"))
    raise SystemExit(1)
