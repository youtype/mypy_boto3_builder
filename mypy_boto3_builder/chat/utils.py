"""
Message-related utils.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.chat.type_defs import Message


def as_string(message: Message | list[tuple[str, str]] | str) -> str:
    """
    Convert message to string.
    """
    if isinstance(message, str):
        return message
    result = (item if isinstance(item, str) else item[1] for item in message)
    return "".join(result)


def as_message(message: Message | str) -> Message:
    """
    Convert message or string to Message.
    """
    if not message:
        return ()
    if isinstance(message, str):
        return (message,)

    return message
