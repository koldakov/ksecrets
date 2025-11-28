from typing import Annotated

import rich
import typer

from ksecrets.services.encryptors.encrypt import EncryptService, EncryptServiceResponse


def encrypt(
    text: Annotated[
        str,
        typer.Argument(
            help="Text to encrypt.",
        ),
    ],
    password: str = typer.Option(
        None,
        "--password",
        "-p",
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
        help="Password for encryption.",
    ),
) -> None:
    service: EncryptService = EncryptService(
        text=text,
        password=password,
    )
    response: EncryptServiceResponse = service()

    rich.print(response.text)
