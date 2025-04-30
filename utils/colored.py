import typing as t
from colorama import init, Fore, Style

# Enable color support on all platforms and auto-reset after each print
init(autoreset=True)

def __format_args(args: t.Iterable, sep: str) -> str:
    """
    Join multiple arguments into a single string.

    Args:
        args (Iterable): Items to be joined.
        sep (str): Separator between items.

    Returns:
        str: The formatted string.
    """
    return sep.join(str(arg) for arg in args)

def print_normal(*args, sep: str = ' ', end: str = '\n') -> None:
    """
    Print text with normal formatting.

    Args:
        *args: Strings or other objects to print.
        sep (str, optional): Separator between items. Defaults to ' '.
        end (str, optional): String appended after the last value. Defaults to '\\n'.
    
    Returns:
        None
    """
    print(__format_args(args, sep), end=end)

def print_error(*args, sep: str = ' ', end: str = '\n') -> None:
    """
    Print text as an error message in red.

    Args:
        *args: Strings or other objects to print.
        sep (str, optional): Separator between items. Defaults to ' '.
        end (str, optional): String appended after the last value. Defaults to '\\n'.
    
    Returns:
        None
    """
    print(f"{Fore.RED}{__format_args(args, sep)}", end=end)

def print_success(*args, sep: str = ' ', end: str = '\n') -> None:
    """
    Print text as a success message in green.

    Args:
        *args: Strings or other objects to print.
        sep (str, optional): Separator between items. Defaults to ' '.
        end (str, optional): String appended after the last value. Defaults to '\\n'.
    
    Returns:
        None
    """
    print(f"{Fore.GREEN}{__format_args(args, sep)}", end=end)

def print_warning(*args, sep: str = ' ', end: str = '\n') -> None:
    """
    Print text as a warning message in yellow.

    Args:
        *args: Strings or other objects to print.
        sep (str, optional): Separator between items. Defaults to ' '.
        end (str, optional): String appended after the last value. Defaults to '\\n'.
    
    Returns:
        None
    """
    print(f"{Fore.YELLOW}{__format_args(args, sep)}", end=end)

def print_debug(*args, sep: str = ' ', end: str = '\n') -> None:
    """
    Print text as a debug message in grey.

    Args:
        *args: Strings or other objects to print.
        sep (str, optional): Separator between items. Defaults to ' '.
        end (str, optional): String appended after the last value. Defaults to '\\n'.
    
    Returns:
        None
    """
    print(f"{Fore.LIGHTBLACK_EX}{__format_args(args, sep)}", end=end)
