from __future__ import annotations

from typing import TYPE_CHECKING

import typer

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence


class Typer(typer.Typer):
    def __init__(
        self,
        command_list: Sequence[Callable],
        /,
        *,
        typer_list: Sequence[typer.Typer] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self._register_typers(typer_list)
        self._register_commands(command_list)

    def _register_typers(self, typer_list: Sequence[typer.Typer] | None, /) -> None:
        if typer_list is None:
            return

        for typer_ in typer_list:
            self.add_typer(typer_)

    def _register_commands(self, command_list: Sequence[Callable], /) -> None:
        for command in command_list:
            self.command(no_args_is_help=True)(command)
