from enum import Enum
from typing import Tuple

import typer

from components import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
)

app = typer.Typer()


def get_version_str(
    title: str = __title__,
    description: str = __description__,
    url: str = __url__,
    version: Tuple[int, int, int] = __version__,
    author: str = __author__,
    author_email: str = __author_email__,
) -> str:
    return f"""# THIS FILE IS GENERATED
# MODIFICATIONS MAY BE LOST
__title__ = "{title}"
__description__ = "{description}"
__url__ = "{url}"
__version__ = {version}
__author__ = "{author}"
__author_email__ = "{author_email}"
    """


class VersionType(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


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
def build(ver: VersionType | None = None) -> None:
    if ver:
        version = bump_version(__version__, ver)
        with open("src/components/__version__.py", "w") as f:
            f.write(get_version_str(version=version))


if __name__ == "__main__":
    app()
