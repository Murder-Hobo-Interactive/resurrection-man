from enum import Enum
from typing import Tuple

import typer

from components import __version__

app = typer.Typer()


def get_version_str(
    title: str = "Resurrection Man",
    description: str = "Grave robbing and other fun things",
    url: str = "https://github.com/Murder-Hobo-Interactive/resurrection-man",
    version: Tuple[int, int, int] = (0, 0, 0),
    author: str = "Chris Palmer",
    author_email="capalmer1013@gmail.com",
) -> str:
    return f"""
    # THIS FILE IS GENERATED
    # MODIFICATIONS MAY BE LOST
    __title__ = {title}
    __description__ = {description}
    __url__ = {url}
    __version__ = {version}
    __author__ = {author}
    __author_email__ = {author_email}
    """


class VersionType(Enum):
    NONE = 0
    MAJOR = 1
    MINOR = 2
    PATCH = 3


def bump_version(
    version: Tuple[int, int, int], version_type: VersionType
) -> Tuple[int, int, int]:
    new_version: Tuple[int, int, int]
    if version_type == VersionType.MAJOR:
        new_version = (version[0] + 1, 0, 0)

    elif version_type == VersionType.MINOR:
        new_version = (version[0], version[1] + 1, 0)

    elif version_type == VersionType.PATCH:
        new_version = (version[0], version[1], version[2] + 1)

    return new_version


@app.command()
def build(ver: int) -> None:
    print(__version__)
    # bump_version(version)
    pass


if __name__ == "__main__":
    app()
