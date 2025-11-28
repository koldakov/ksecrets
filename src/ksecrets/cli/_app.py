from ._typer import Typer
from .commands import command_list, typer_list

app: Typer = Typer(
    command_list,
    typer_list=typer_list,
)
