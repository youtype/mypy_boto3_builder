"""
Type annotations for Chat.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from collections.abc import MutableSequence

from mypy_boto3_builder.chat.text_style import TextStyle

MessagePair = tuple[TextStyle, str]
MessageToken = MessagePair | str
Message = tuple[MessageToken, ...] | MutableSequence[MessageToken]
