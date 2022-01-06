"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    Machine for finding random words from a dictionary.

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() -> Provides with random word

    """

    def __init__(self, path):
        """Open file and print word"""

        txt_file = open(path)

        self.words = self.parse(txt_file)

        print(f"{len(self.words)} words read")

    def parse(self, txt_file):
        """Parse into list of words stripped of newlines"""
        return [line.strip() for line in txt_file]


    def random(self):
        """Return random word"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Does not read blanks and comments"""

    def parse(self, txt_file):
        """Does not read blanks and comments"""

        return [line.strip() for line in txt_file if line.strip() and not line.startswith("#")]