from .grammar import Program

def interpret(statement) -> Program:
    print(f"{statement}: not found")
    return Program.LOOP
