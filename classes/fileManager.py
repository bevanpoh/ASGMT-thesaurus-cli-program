# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from pathlib import Path
from classes.utils.errors import FilenameError
from classes.utils.userInput import UserInput
from classes.file import File


# Handles File IO operations e.g. Writng, Reading, Creating to the root folder
class FileManager:
    __rootpath = Path(f"{Path.cwd()}/data")

    # =============================================================== #
    # Class Methods
    # =============================================================== #
    def __validatePathRoot(file):
        path = Path(FileManager.__rootpath, file.name)

        # dont allow directory traversal
        if FileManager.__rootpath not in path.parents:
            raise FilenameError("Invalid filename!")

        return path

    def createFileFromInput(message="Please enter input file: "):
        while True:
            filename = input(message)

            if not filename:
                if (
                    UserInput.YesOrNo("Do you want to abort entering a file?")
                    == "y"
                ):
                    return None
                else:
                    continue  # goto input filename

            try:
                file = File(filename)
            except Exception as e:
                UserInput.acknowledgeError(e)
            else:
                return file

    def readFromFile(file):
        try:
            pathToLoad = FileManager.__validatePathRoot(file)
            try:
                fileContent = pathToLoad.read_text()
            except UnicodeDecodeError:
                try:
                    fileContent = pathToLoad.read_text(encoding="utf-8")
                except:
                    fileContent = pathToLoad.read_text(errors="replace")

        except FileNotFoundError:
            raise FileNotFoundError(f'File "{file.name}" not found!')

        except OSError:
            raise OSError(f'File "{file.name}" could not be opened!')

        return fileContent

    def writeToFile(file, content):
        if file.exists():
            overwrite = UserInput.YesOrNo(
                f'File "{file}" already exists. Do you want to overwrite it?'
            )

            if not overwrite:
                return

        try:
            pathToWrite = FileManager.__validatePathRoot(file)

            try:
                pathToWrite.write_text(str(content))
            except UnicodeEncodeError:
                try:
                    pathToWrite.write_text(str(content), encoding="utf-8")
                except:
                    pathToWrite.write_text(str(content), errors="replace")

        except FileNotFoundError:
            raise FileNotFoundError(f'File "{file.name}" not found!')

        except OSError:
            raise OSError(f'Error saving to "{file.name}"!')

    def readFileSize(file):
        pathToRead = FileManager.__validatePathRoot(file)
        return f"File size: {File(pathToRead).size}"

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Methods
    # =============================================================== #
