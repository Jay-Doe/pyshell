from .model import Command


def tokenize(sentence: str) -> list[str]:
    return sentence.strip().split(" ")


def parse(words: list[str]) -> Command:
    if not words:
        print("no command found")
        raise Exception("empty input exception")

    name, *args = words
    return Command(name, tuple(args))
