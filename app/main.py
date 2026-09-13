import sys
from app.interpreter.grammar import Program
from app.interpreter.tokenizer import tokenize
from app.interpreter.interpreter import interpret


def main():
    shell_state  = Program.LOOP
    while (shell_state == Program.LOOP ):
        sys.stdout.write("$ ")
        sentence =  input()
        words = tokenize(sentence)
        shell_state = interpret(words)



if __name__ == "__main__":
    main()
