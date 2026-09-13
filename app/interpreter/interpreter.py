from .grammar import Program

def interpret(statement: list[str]) -> Program:
    print(f"{statement[0]}: not found")
    return Program.LOOP
