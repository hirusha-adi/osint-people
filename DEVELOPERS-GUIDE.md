# Developer's Guide

This is just something like a rule-set for developer's to follow while adding new modules or modifying the existing modules. The goal is to make everything, including but not limited to the user experience consistent.

## Input

All the inputs MUST be taken as CLI arguments. You should not use the `input()` function to get any user input.

## Output

All the functions listed below have been well documented, though it's very simple and self-explanatory.

**General Messages**
Use `utils.colored.print_normal()`. Just the normal `print()`. Try to stick with the other functions whenever and wherever possible.

**Errors**
Use `utils.colored.print_error()`. Must be printed in red color if supported.

**Success**
Use `utils.colored.print_success()`. Must be printed in green color if supported.

**Warnings**
Use `utils.colored.print_warning()`. Must be printed in yellow color if supported.

**Debug Messages**
Use `utils.colored.print_debug()`. Must be printed in grey color if supported.
