"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    ...
    def __init__(self, path):
        """reads the file, and reports the number of words it read"""

        dict_file = open(path)

        self.words = self.only_word(dict_file)

        print(f"{len(self.words)} words read")

    def only_word(self, dict_file):
        """turns file into a list of words"""

        return [w.strip() for w in dict_file]

    def random(self):
        """retruns random word"""

        return random.choice(self.words)



class SpecialWordFinder(WordFinder):
    
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def only_word(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]