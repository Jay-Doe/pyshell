from app.p_domain.exe import find_exe
from .grammar import BUILTINS
from collections.abc import Callable
from .grammar import Program, Statement, CmdType

type Executor = Callable[[Statement], Program]

def interpret(statement: Statement) -> Program:
        f = DispatchTable[statement.type]
        return f(statement)




def exe_not_found(statement: Statement) -> Program:
    print(f"{statement.cmd}: command not found")
    return Program.LOOP

def exe_builtin(statement: Statement) -> Program:
    match(statement.cmd):
        case "exit":
            return Program.EXIT
        case "echo":
            print(" ".join(statement.args))
            return Program.LOOP
        case "type":
            x = statement.args[0]
            if x in BUILTINS:
                print(f"{x} is a shell builtin")
                return Program.LOOP
            if x:
                y = find_exe(x)
                if y:
                    print(f"{x}: is {y}")
                    Program.LOOP
            print(f"{x}: not found")
            return Program.LOOP

        case _:
            raise NotImplementedError("Builtin not implemented yet")


def lex(words: list[str]) -> Statement:
    if not words:
        print("no command found")
        raise Exception("empty input exception")

    cmd, *args = words
    type = categorize(cmd)
    return Statement(cmd, type, args)


def categorize(cmd: str) -> CmdType:
    if cmd in BUILTINS:
        return CmdType.BUILTIN
    return CmdType.NOT_FOUND

DispatchTable: dict[CmdType, Executor] = {
    CmdType.BUILTIN : exe_builtin,
    CmdType.NOT_FOUND: exe_not_found,

}
