from collections.abc import Callable, Sequence

from ._encrypt import encrypt

command_list: Sequence[Callable] = [
    encrypt,
]

__all__ = [
    "command_list",
]
