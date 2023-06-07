# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
from msvcrt import getch

# User input-related methods
class UserInput:
    # =============================================================== #
    # Class Methods
    # =============================================================== #
    # Validates menu number selection
    def option(message="Enter choice: "):
        while True:
            try:
                option = int(input(message))
            except ValueError:
                UserInput.acknowledgeError("Please select a number!")
            else:
                return option

    # Halts program and waits for button press
    def anyKey(message="Press any key to continue...."):
        print()
        print(message)
        getch()
        print()

    # Prints error message and waits for user acknowledgement
    def acknowledgeError(errMsg, message="Press 'Enter' to continue..."):
        print()
        print(errMsg)
        input(message)
        print()

    # Asks y/n question and validates user input
    def YesOrNo(message):
        while True:
            response = input(f"{message} y/n: ").lower().strip()

            if response and (response == "y" or response == "n"):
                return response

            UserInput.acknowledgeError("Invalid option!")

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Methods
    # =============================================================== #
