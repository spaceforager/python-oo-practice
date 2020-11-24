"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:

    def __init__(self, path):

        file_open = open(path, 'r')
        self.words = self.parse(file_open)
        print(f"{len(self.words)} words read")

    def parse(self, file_open):
        """return list of words with leading and trailing characters removed"""
        return [line.strip() for line in file_open]

    def random(self):
        """return random word"""
        return choice(self.words)


class RandomWordFinder(WordFinder):

    def parse(self, file_open):
        return [line.strip() for line in file_open if line.strip() and not line.startswith('#')]
