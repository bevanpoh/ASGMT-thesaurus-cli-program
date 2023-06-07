# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

import regex as re # unicode support
# regex is included in base anaconda but not base py3.9
# https://docs.anaconda.com/anaconda/packages/old-pkg-lists/2021.04/py3.9_win-64/
import random

# Receives a thesaurus and prepares it for lookup of matches and their replacements
# Has methods to act on and process text in arguments
class TextProcessor:
    __wordPattern = re.compile("\p{L}+")

    def __init__(self, thesaurus):
        self.__thesaurus = thesaurus
        self.__reversedThesaurus = self.__reverse(thesaurus)

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        return

    # =============================================================== #
    # Methods
    # =============================================================== #
    def __reverse(self, thesaurus):
        # changes thesaurus to syn: keyword for quick lookup and replacement
        # from {key1: [syn1, syn2, syn3, ...], key2:[syn1, ...]}
        # to {syn1: [key1, key2], syn2: [key1], syn3:[key1], ...}

        reversed = dict()
        for key in thesaurus:
            for item in thesaurus[key]:
                if item not in reversed:
                    reversed[item] = [key]
                else:
                    reversed[item].append(key)
        return reversed

    def __kwToSyn(self, matchObj):
        match = matchObj.group(0)

        if match.lower() in self.__thesaurus:  # keyword match
            replacement = random.choice(self.__thesaurus[match.lower()])

            if match[0].isupper():
                return replacement.capitalize()
            else:
                return replacement
        else:
            return match

    def __synToKw(self, matchObj):
        match = matchObj.group(0)

        if match.lower() in self.__reversedThesaurus:  # synonym match
            replacement = random.choice(self.__reversedThesaurus[match.lower()])

            if match[0].isupper():
                return replacement.capitalize()
            else:
                return replacement
        else:
            return match

    def replace(self, text, method):
        if method == "elegant":
            replaced = TextProcessor.__wordPattern.sub(self.__kwToSyn, text)
        elif method == "simple":
            replaced = TextProcessor.__wordPattern.sub(self.__synToKw, text)
        else:
            raise NotImplementedError(f'Invalid processing option "{method}"!')

        return replaced
