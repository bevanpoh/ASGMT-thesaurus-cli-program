# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================


import regex as re # unicode support
# regex is included in base anaconda but not base py3.9
# https://docs.anaconda.com/anaconda/packages/old-pkg-lists/2021.04/py3.9_win-64/
from classes.synonyms import Synonyms
from classes.synonym import Synonym
from classes.thesaurus import Thesaurus
from classes.utils.errors import DuplicateError
from classes.utils.userInput import UserInput

# Receives and Processesinputs for Thesaurus keywords amd Synonyms
# Passes formatted data to Thesaurus and Synonyms
class ThesaurusManager:
    __lineSep = re.compile("\n")

    # `:` between any whitespace
    __keySep = re.compile("\s*:\s*")
    # `,` between any whitespace
    __synSep = re.compile("\s*,\s*")

    # =============================================================== #
    # Class Methods
    # =============================================================== #
    def createFromInput():
        thes = Thesaurus()

        while True:
            key = input("Enter keyword: ")

            if key:
                try:
                    thes.addKeyword(key)
                except Exception as e:
                    UserInput.acknowledgeError(e)
                    continue  # goto enter keyword

                print()
                print(f"You may enter one or more synonyms for \"{key}\"")
                print("Please press \"Enter\" once done")
                while True:
                    syn = input(f"Enter synonym for \"{key}\": ")

                    if syn:
                        try:
                            thes[key].insertSynonym(Synonym(syn))
                        except Exception as e:
                            UserInput.acknowledgeError(e)
                            continue  # goto enter synonym

                    # if syn is "" has three outcomes:
                    # 1. remove kw if it will be empty and user wants and exit loop
                    # 2. go back to asking for synonyms loop if user doesn't want
                    # 3. ask for more keywords if kw is not empty
                    else:
                        if len(thes[key]) == 0:
                            if UserInput.YesOrNo(f"Do you want to remove {key}") == "y":
                                thes.pop(key)
                                break  # goto otuside loop
                            else:
                                continue
                        break  # goto otuside loop

            if len(thes) == 0:
                if (
                    UserInput.YesOrNo(f"Do you want to abort creating a Thesaurus?")
                    == "y"
                ):
                    return None

            elif UserInput.YesOrNo(f"Do you want to add more keywords?") == "n":
                return thes

    def parseText(text):
        thes = Thesaurus()

        lines = ThesaurusManager.__lineSep.split(text.lower().strip())

        for line in lines:
            try:  # try unpacking
                keyword, synonyms = ThesaurusManager.__keySep.split(line)
            except ValueError as e:
                raise ValueError("Invalid Thesaurus format provided")

            synonyms = [
                Synonym(syn) for syn in ThesaurusManager.__synSep.split(synonyms)
            ]

            try:
                syns = Synonyms(synonyms)
            except DuplicateError as e:
                raise DuplicateError(f'{e} for keyword "{keyword}"')

            thes[keyword] = syns

        return thes

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Methods
    # =============================================================== #
