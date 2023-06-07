# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
from classes.data_structures.sortedArray import SortedArray

# A dictionary whose keys can be maintained in a sorted order
# Used by Thesaurus class
class sortedDict(dict):
    def __init__(self):
        super().__init__()
        self.__sortedKeys = SortedArray()

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self): # access in order of sorted keys
        output = ", ".join(f"{key}: {self[key]}" for key in self.keys())

        return output

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__sortedKeys.insert(key)

    def __contains__(self, key):
        return key in self.keys()

    # =============================================================== #
    # Methods
    # =============================================================== #
    def keys(self):
        return self.__sortedKeys

    def pop(self, item):
        super().pop(item)
        self.__sortedKeys.remove(item)
