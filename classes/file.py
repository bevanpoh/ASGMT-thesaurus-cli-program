# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================
from pathlib import Path
from classes.utils.errors import UnsupportedFormatError


# File object that receives and stores a filename
# validates filename extension and format
class File:
    validFormats = {".txt"}

    def __init__(self, filename):
        self.setFilename(filename)

    # =============================================================== #
    # Properties
    # =============================================================== #
    @property
    def name(self):
        return self.__filename.name

    @property
    def size(self):
        return f"{self.__filename.stat().st_size/1024:.2f} KB"

    def setFilename(self, filename):
        filename = Path(filename)

        extension = filename.suffix
        if extension not in File.validFormats:
            raise UnsupportedFormatError(
                f"File format not supported!\n Currently only {', '.join(File.validFormats)} files are supported"
            )

        self.__filename = filename

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        return self.name

    # =============================================================== #
    # Methods
    # =============================================================== #
    def exists(self):
        return self.__filename.exists()
