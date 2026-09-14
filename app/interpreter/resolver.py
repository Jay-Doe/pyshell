import os
from pathlib import Path

from .context import ShellContext


def resolve_executable(name: str, context: ShellContext) -> Path | None:
    for path_entry in context.path:
        directory = Path(path_entry) if path_entry else context.cwd
        if not directory.is_absolute():
            directory = context.cwd / directory

        executable = directory / name
        if executable.exists() and os.access(executable, os.X_OK):
            return executable

    return None
