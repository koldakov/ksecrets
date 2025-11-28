from collections.abc import Callable, Sequence

from ._decrypt import decrypt

command_list: Sequence[Callable] = [
    decrypt,
]

__all__ = [
    "command_list",
]
