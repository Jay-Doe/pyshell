import sys

from app.interpreter.context import initial_context
from app.interpreter.model import Program
from app.interpreter.parser import parse, tokenize
from app.interpreter.runtime import execute


def main():
    context = initial_context()
    program = Program.LOOP
    while program == Program.LOOP:
        sys.stdout.write("$ ")
        sentence = input()
        words = tokenize(sentence)
        command = parse(words)
        result = execute(command, context)
        sys.stdout.write(result.output)
        context = result.context
        program = result.program

if __name__ == "__main__":
    main()
