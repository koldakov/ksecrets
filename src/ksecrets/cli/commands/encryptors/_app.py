from ksecrets.cli._typer import Typer

from .commands import command_list

app: Typer = Typer(command_list)
