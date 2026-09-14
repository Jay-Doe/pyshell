import subprocess
from pathlib import Path

from .builtins import BUILTINS, execute_builtin
from .context import ShellContext
from .model import Command, ExecutionResult, Program
from .resolver import resolve_executable


def execute(command: Command, context: ShellContext) -> ExecutionResult:
    if command.name in BUILTINS:
        return execute_builtin(command, context)

    executable = resolve_executable(command.name, context)
    if executable is None:
        return ExecutionResult(
            context,
            Program.LOOP,
            f"{command.name}: command not found\n",
        )

    return execute_external(command, context, executable)


def execute_external(
    command: Command,
    context: ShellContext,
    executable: Path | None,
) -> ExecutionResult:
    if executable is None:
        raise AttributeError(
            "An executable statement is missing a path, "
            "this should have been caught earlier"
        )

    process = subprocess.Popen(
        [command.name, *command.args],
        cwd=context.cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    if process.stdout is not None:
        for line in process.stdout:
            print(line, end="")

    return ExecutionResult(context, Program.LOOP)
