# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
from classes.data_structures.sortedArray import SortedArray
from classes.utils.errors import DuplicateError


# Stores Synonym objects and maintain their sorted order
class Synonyms(SortedArray):
    def __init__(self, words=None):
        if words:
            duplicates = self.__findDuplicates(words)
            if duplicates:
                raise DuplicateError(f"Duplicate synonyms {duplicates} found")

            self.__lookup = set(words)
            super().__init__(words)
        else:
            self.__lookup = set()
            super().__init__()

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        return ", ".join(self)

    def __contains__(self, synonym):
        return synonym in self.__lookup

    # =============================================================== #
    # Methods
    # =============================================================== #
    def insertSynonym(self, synonym):
        if synonym in self:
            raise DuplicateError(f'Synonym "{synonym}" already exists')

        self.__lookup.add(synonym)
        super().insert(synonym)

    # checks incoming list of words for duplicates
    def __findDuplicates(self, words):
        seen = set()
        seen_twice = set()
        for synonym in words:
            if synonym in seen:
                seen_twice.add(synonym)
            else:
                seen.add(synonym)

        if len(seen_twice) > 0:
            return seen_twice

        return None
