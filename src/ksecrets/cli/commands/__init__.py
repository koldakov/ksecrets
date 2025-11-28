from collections.abc import Callable, Sequence

import typer

from .decryptors._app import app as decryptor_app
from .encryptors._app import app as encryptor_app

command_list: Sequence[Callable] = []
typer_list: Sequence[typer.Typer] = [
    encryptor_app,
    decryptor_app,
]

__all__ = [
    "command_list",
    "typer_list",
]
