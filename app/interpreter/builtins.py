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
    
    if len(cmd.args) == 0:
        return ExecutionResult(
            context=ctx,
            program=Program.LOOP,
            output="cd: missing argument\n",
        )
    target = cmd.args[0]
    if "~" in target:
        target = Path(target).expanduser()
    absolute = Path(target).is_absolute()
    if  absolute and Path(target).exists():
        ctx = ShellContext(
            cwd=Path(target),
            path=ctx.path,
            home=ctx.home,
        )
        return ExecutionResult(context=ctx, program=Program.LOOP, output="")


    elif not absolute:
        maybe_target = os.path.normpath(ctx.cwd / target)
        if Path(maybe_target).exists():
            ctx = ShellContext(
                cwd=Path(maybe_target),
                path=ctx.path,
                home=ctx.home,
            )
            return ExecutionResult(context=ctx, program=Program.LOOP, output="")

    return ExecutionResult(
            context=ctx,
            program=Program.LOOP,
            output=f"cd: {target}: No such file or directory\n",
        )


