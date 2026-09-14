from .context import ShellContext
from .model import Command, ExecutionResult, Program, ShellContext
from .resolver import resolve_executable

BUILTINS = ("cd", "exit", "type", "echo")


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
        case _:
            raise NotImplementedError("Builtin not implemented yet")

def pwd(cmd: Command, ctx: ShellContext) -> ExecutionResult:

    return ExecutionResult(context=ctx, program=Program.LOOP, output=(str(ctx.cwd)+"\n"))
