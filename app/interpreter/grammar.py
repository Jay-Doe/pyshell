from enum import Enum, auto

BUILTINS = ("cd", "exit", "type", "echo")

class Program(Enum):
    EXIT = auto()
    LOOP = auto()
