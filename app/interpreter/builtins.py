import os
from pathlib import Path

from .context import ShellContext
from .model import Command, ExecutionResult, Program
from .resolver import resolve_executable

BUILTINS = ("pwd", "cd", "exit", "type", "echo")


def execute_builtin(command: Command, context: ShellContext) -> ExecutionResult:
    match command.name:
        case "exit":
            return ExecutionResult(context, Program.EXIT)
        case "echo":
            return ExecutionResult(
                context,
                Program.LOOP,
                " ".join(command.args) + "\n",
            )
        case "type":
            name = command.args[0]
            if name in BUILTINS:
                return ExecutionResult(
                    context,
                    Program.LOOP,
                    f"{name} is a shell builtin\n",
                )

            executable = resolve_executable(name, context) if name else None
            if executable:
                return ExecutionResult(
                    context,
                    Program.LOOP,
                    f"{name} is {executable}\n",
                )

            return ExecutionResult(
                context,
                Program.LOOP,
                f"{name}: not found\n",
            )
        case "pwd":
            return pwd(command, context)
        case "cd":
            return cd(command, context)
        case _:
            raise NotImplementedError("Builtin not implemented yet")

def pwd(cmd: Command, ctx: ShellContext) -> ExecutionResult:

    return ExecutionResult(context=ctx, program=Program.LOOP, output=(str(ctx.cwd)+"\n"))

def cd(cmd: Command, ctx: ShellContext) -> ExecutionResult:
    
    if not cmd.args:
        return ExecutionResult(
            context=ctx,
            program=Program.LOOP,
            output="cd: missing argument\n",
        )
    raw = cmd.args[0]
    path = Path(raw).expanduser()
    absolute = Path(target).is_absolute()
    if not absolute:
        path = ctx.cwd /path
    path = Path(os.path.normpath(path))
    if path.is_dir():
        return ExecutionResult(
            context=ShellContext(
                cwd=path,
                path=ctx.path,
                home=ctx.home,
            ),
            program=Program.LOOP,
        )
                
    return ExecutionResult(
            context=ctx,
            program=Program.LOOP,
            output=f"cd: {raw}: No such file or directory\n",
        )


