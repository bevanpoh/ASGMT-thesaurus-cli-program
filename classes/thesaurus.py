# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
from classes.data_structures.sortedDict import sortedDict
from classes.synonyms import Synonyms
from classes.synonym import Synonym
from classes.utils.errors import DuplicateError


# Stores keyword and Synonyms object pairs

class Thesaurus(sortedDict):
    def __init__(self):
        super().__init__()

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        return "\n".join(f"{key}: {self[key]}" for key in self.keys())

    def __setitem__(self, key, value):
        if not key.isalpha():
            raise KeyError(f'Keyword "{key}" is not a valid word!')

        if key in self:
            raise DuplicateError(f'Keyword "{key}" already exists!')

        super().__setitem__(key, value)

    def __getitem__(self, __key):
        return super().__getitem__(__key)

    # =============================================================== #
    # Methods
    # =============================================================== #
    def addKeyword(self, keyword):
        self[keyword] = Synonyms()

    def sort(self, sortCriteria):
        # set active sorting criteria in Synonym class
        Synonym.setSortCriteria(sortCriteria)

        for keyword in self:
            self[keyword].sort()

    def shuffle(self):
        for keyword in self:
            self[keyword].shuffle()
