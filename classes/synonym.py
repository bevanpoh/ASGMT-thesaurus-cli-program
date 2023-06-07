# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
import random

# Wrapper around a string to support
# dynamic custom comparisons

class Synonym(str):
    def __new__(cls, string):
        if not string.isalpha():
            raise ValueError(f'Invalid synonym "{string}"!')

        instance = super().__new__(cls, string)
        return instance

    __activeSortCriteria = ("alpha", "alpha")

    # lambda function that wrap around self and other when making comparisons
    __sortKeys = {
        "alpha": lambda word: str(word),
        "length": lambda word: len(word),
        "random": lambda _: random.random(),
    }

    # =============================================================== #
    # Class Properties
    # =============================================================== #
    def setSortCriteria(sorts):
        try:
            primarySort, secondarySort = sorts
        except Exception as e:
            raise Exception(f"Invalid sort criteria {sorts}") from e

        for sort in sorts:
            if sort not in Synonym.__sortKeys:
                raise NotImplementedError(f'Sort criteria "{sort}" not implemented!')

        Synonym.__activeSortCriteria = (primarySort, secondarySort)

    # =============================================================== #
    # Class Methods
    # =============================================================== #
    def __extractActiveKeys():
        primarySortKey, secondarySortKey = (
            Synonym.__sortKeys[sortCriterion]
            for sortCriterion in Synonym.__activeSortCriteria
        )

        return primarySortKey, secondarySortKey

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    # __hash__ to accomodate set() and in operations
    def __hash__(self):
        return super().__hash__()

    def __lt__(self, other):
        primarySortKey, secondarySortKey = Synonym.__extractActiveKeys()

        if primarySortKey(self) < primarySortKey(other):
            return True
        elif primarySortKey(self) == primarySortKey(other):
            return secondarySortKey(self) < secondarySortKey(other)
        else:
            return False

    def __gt__(self, other):
        primarySortKey, secondarySortKey = Synonym.__extractActiveKeys()

        if primarySortKey(self) > primarySortKey(other):
            return True
        elif primarySortKey(self) == primarySortKey(other):
            return secondarySortKey(self) > secondarySortKey(other)
        else:
            return False

    def __le__(self, other):
        primarySortKey, secondarySortKey = Synonym.__extractActiveKeys()

        if primarySortKey(self) < primarySortKey(other):
            return True
        elif primarySortKey(self) == primarySortKey(other):
            return secondarySortKey(self) <= secondarySortKey(other)
        else:
            return False

    def __ge__(self, other):
        primarySortKey, secondarySortKey = Synonym.__extractActiveKeys()

        if primarySortKey(self) > primarySortKey(other):
            return True
        elif primarySortKey(self) == primarySortKey(other):
            return secondarySortKey(self) >= secondarySortKey(other)
        else:
            return False

    # =============================================================== #
    # Methods
    # =============================================================== #


if __name__ == "__main__":
    yn = Synonym("Apple")
    print(yn)
    print(type(yn))
