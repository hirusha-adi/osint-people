import os
from utils import decorators
from utils import colored


@decorators.handle_errors
def start(email: str, color=False, clear=False) -> None:
    colored.print_info(f"Running holehe with email: {email}")
    
    cmd = f"holehe {'--no-color' if not color else ''} {'--no-clear' if not clear else ''} {email}"
    exit_code = os.system(cmd)

    if exit_code == 0:
        colored.print_success("Successfully ran holehe.")
    else:
        colored.print_error("An error occurred while running holehe.")
