"""
Multiple string utils collection.
"""
from typing import List


def get_class_prefix(func_name: str) -> str:
    """
    Get a valid Python class prefix from `func_name`.

    Arguments:
        func_name -- Any string.

    Returns:
        String with a class prefix.
    """
    parts = [f"{i[:1].upper()}{i[1:]}" for i in func_name.split("_") if i]
    return "".join(parts)


def get_line_with_indented(input_string: str, multi_first_line: bool = False) -> str:
    """
    Get first line of the string with all indented lines.

    Fixes invalid unindent.

    Arguments:
        input_string -- Input string.

    Returns:
        A string with first line and following indented lines.
    """
    result: List[str] = []
    indent_stack: List[int] = []
    for line in input_string.splitlines():
        line_indent = len(line) - len(line.lstrip())
        if not indent_stack:
            indent_stack.append(line_indent)
            result.append(line)
            continue

        if not line:
            result.append(line)
            continue

        if line_indent < indent_stack[0]:
            break

        if line_indent == indent_stack[0]:
            if not multi_first_line:
                break

            if len(indent_stack) > 1:
                break

        if line_indent == indent_stack[-1]:
            result.append(line)
            continue

        if line_indent > indent_stack[-1]:
            indent_stack.append(line_indent)
            result.append(line)
            continue

        while len(indent_stack) > 1 and line_indent <= indent_stack[-2]:
            indent_stack.pop()

        if indent_stack[-1] != line_indent:
            result.append(f"{' ' * indent_stack[-1]}{line[line_indent:]}")
            continue

        result.append(line)

    while result and not result[-1]:
        result.pop()

    return "\n".join(result)
