import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ShellContext:
    cwd: Path
    path: tuple[str, ...]
    home: Path


def initial_context() -> ShellContext:
    return ShellContext(
        cwd=Path.cwd(),
        path=tuple(os.environ.get("PATH", "").split(os.pathsep)),
        home=Path.home(),
    )
