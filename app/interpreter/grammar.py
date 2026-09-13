from enum import Enum, auto
from dataclasses import dataclass

BUILTINS = ("cd", "exit", "type", "echo")

class Program(Enum):
    EXIT = auto()
    LOOP = auto()

class CmdType(Enum):
    BUILTIN = auto()
    EXE = auto()
    NOT_FOUND = auto()

@dataclass(frozen=True)
class Statement:
    cmd: str
    type: CmdType
    args: list[str]
    path: str | None = None
