# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================


# Stores option number: option name pairs
# Simply displays Menu UI
class DisplayMenu(dict):
    def __init__(self, options):
        for i, option in enumerate(options):
            self[i + 1] = option

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        output = f"Please select your choice: {tuple(range(1,len(self)+1))}\n"
        output += "\n".join(
            f"\t{option_num}: {option_name}" for option_num, option_name in self.items()
        )

        return output

    # =============================================================== #
    # Methods
    # =============================================================== #

    def appendOption(self, option):
        self[len(self) + 1] = option
