import sys
from app.interpreter.grammar import Program, Statement
from app.interpreter.tokenizer import tokenize
from app.interpreter.interpreter import interpret, lex


def main():
    p  = Program.LOOP
    while (p == Program.LOOP ):
        sys.stdout.write("$ ")
        sentence =  input()
        words = tokenize(sentence)
        statement: Statement = lex(words)
        p = interpret(statement)




if __name__ == "__main__":
    main()
