from dataclasses import dataclass
from enum import Enum, auto

from .context import ShellContext


class Program(Enum):
    EXIT = auto()
    LOOP = auto()


@dataclass(frozen=True, slots=True)
class Command:
    name: str
    args: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    context: ShellContext
    program: Program
    output: str = ""
