from typing import Annotated

import rich
import typer

from ksecrets.services.decryptors.decrypt import DecryptService, DecryptServiceResponse


def decrypt(
    text: Annotated[
        str,
        typer.Argument(
            help="Text to decrypt.",
        ),
    ],
    password: str = typer.Option(
        None,
        "--password",
        "-p",
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
        help="Password for decryption.",
    ),
) -> None:
    service: DecryptService = DecryptService(
        text=text,
        password=password,
    )
    response: DecryptServiceResponse = service()

    rich.print(response.text.get_secret_value())
