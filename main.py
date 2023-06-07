from classes.utils.userInput import UserInput
from classes.fileManager import FileManager
from classes.thesaurusManager import ThesaurusManager
from classes.textProcessor import TextProcessor
from classes.displayMenu import DisplayMenu
import time

print(f"{'*'*60}")
print(f"* {'ST1507 DSAA: Welcome To:':<57}*")
print(f"* {'':<57}*")
print(f"* {'~ Thesaurus Based Text Processing Application ~':<57}*")
print(f"* {'':-<57}*")
print(f"* {'':<57}*")
print(f"* {'- Done by: Bevan Poh(2112745)':<57}*")
print(f"* {'- Class: DAAA/2B/02':<57}*")
print(f"{'*'*60}")
print()
UserInput.anyKey()

thes = None
thesFile = None
text = None
textFile = None
textProcessor = None

mainMenu = DisplayMenu(
    [
        "New",
        "Open",
        "Sort",
        "Process Text",
        "-Not Implemented-",
        "-Not Implemented-",
        "Print",
        "Save",
        "Save As",
        "Exit",
    ]
)
sortMenu = DisplayMenu(
    [
        "Alphabetically (Default)",
        "Length/Alphabetically",
        "Length/Random ALphabetically",
        "Randomly",
        "Back to Main Menu",
    ]
)
processMenu = DisplayMenu(
    ["Simplified Writing", "Elegant Writing", "Back to Main Menu"]
)

while True:
    print(mainMenu)
    mainOption = UserInput.option()
    print()

    if mainOption == 10:
        break
    elif mainOption not in mainMenu:
        UserInput.acknowledgeError("Option out of range!")

    # New
    elif mainOption == 1:
        if (
            thes is not None
            and UserInput.YesOrNo("Do you want to overwrite your existing Thesaurus?")
            == "n"
        ):
            continue

        print()
        print("We will be starting a new Thesaurus")
        print("You may now enter a series of ketwords and their synonyms")
        print()
        thes = ThesaurusManager.createFromInput()

        if thes:
            print("Your new Thesaurus is ready and printed here...")
            print(thes)
            print()

    # Open
    elif mainOption == 2:
        if (
            thes is not None
            and UserInput.YesOrNo("Do you want to overwrite your existing Thesaurus?")
            == "n"
        ):
            continue

        print()
        print("We will be opening an existing Thesaurus")
        tempFile = FileManager.createFileFromInput()

        if not tempFile:
            continue

        try:
            thesText = FileManager.readFromFile(tempFile)
            thes = ThesaurusManager.parseText(thesText)
        except Exception as e:
            UserInput.acknowledgeError(e)
        else:
            thesFile = tempFile
            print()
            print(f'Thesaurus "{thesFile}" has been loaded and is printed here...')
            print(thes)
            print()

    # Sort
    elif mainOption == 3:
        if thes is None:
            UserInput.acknowledgeError("No open Thesaurus to sort!")
            continue

        while True:
            print(sortMenu)
            sortOption = UserInput.option()

            if sortOption == 5:
                break
            elif sortOption not in sortMenu:
                UserInput.acknowledgeError("Option out of range!")
                continue

            else:
                print(f"Sorting Synonyms: {sortMenu[sortOption]}")
                print()
                if sortOption == 1:
                    thes.sort(("alpha", "alpha"))
                elif sortOption == 2:
                    thes.sort(("length", "alpha"))
                elif sortOption == 3:
                    thes.sort(("length", "random"))
                elif sortOption == 4:
                    thes.shuffle()

            print(thes)
            print()
            UserInput.anyKey()

    # Process Text
    elif mainOption == 4:
        if thes is None:
            UserInput.acknowledgeError("No open Thesaurus to use!")
            continue

        TEXTLIMIT = 10000
        while True:
            if (
                text is None
                or UserInput.YesOrNo(f'Do you want to keep using text "{textFile}"?')
                == "n"
            ):
                print()
                print("Select the file you want to process")
                try:
                    textFile = FileManager.createFileFromInput()
                    text = FileManager.readFromFile(textFile)
                    textProcessor = TextProcessor(thes)
                except Exception as e:
                    UserInput.acknowledgeError(e)
                    continue

            # from empty input
            if text is None:
                continue

            print()
            print("The text before processing: ")

            print(text[:TEXTLIMIT])
            if len(text) > TEXTLIMIT:
                print(f"First {TEXTLIMIT} characters are printed above")

            print(FileManager.readFileSize(textFile))
            UserInput.anyKey()
            print("Next choose a Text Processing Option")
            print()

            print(processMenu)
            processOption = UserInput.option()

            if processOption == 3:
                break
            elif processOption not in processMenu:
                UserInput.acknowledgeError("Option out of range!")
                continue

            print()
            print(f"Processing text for: {processMenu[processOption]}")
            print()

            start = time.perf_counter()
            if processOption == 1:
                replaced = textProcessor.replace(text, "elegant")
            elif processOption == 2:
                replaced = textProcessor.replace(text, "simple")
            end = time.perf_counter()

            print()
            print("The text after processing:")

            print(replaced[:TEXTLIMIT])
            if len(replaced) > TEXTLIMIT:
                print(f"First {TEXTLIMIT} characters are printed above")

            print(f"Time taken to replace: {end-start:.2f}s")
            UserInput.anyKey()

            if UserInput.YesOrNo("Do you want to save text to file?") == "n":
                continue

            textFileToSave = FileManager.createFileFromInput()

            try:
                FileManager.writeToFile(textFileToSave, replaced)
            except Exception as e:
                UserInput.acknowledgeError(e)

    # Bonus options
    elif mainOption == 5 or mainOption == 6:
        UserInput.acknowledgeError(f"Option {mainOption} not implemented!")

    # Print
    elif mainOption == 7:
        print()
        if thes is None:
            UserInput.acknowledgeError("No open Thesaurus to print!")
            continue

        if thesFile is not None:
            thesaurusName = f'The Thesaurus "{thesFile}"'
        else:
            thesaurusName = "Your Thesaurus"

        print(f"{thesaurusName} is printed here...")
        print(thes)

    # Save
    elif mainOption == 8:
        if thes is None:
            UserInput.acknowledgeError("No open Thesaurus to save!")
            continue
        if thesFile is None:
            UserInput.acknowledgeError("No open file to save!")
            continue

        print(mainMenu[mainOption])
        try:
            FileManager.writeToFile(thesFile, str(thes))
        except Exception as e:
            UserInput.acknowledgeError(e)
        else:
            print(f'Successfully saved to "{thesFile}"')

    # Save As
    elif mainOption == 9:
        if thes is None:
            UserInput.acknowledgeError("No open Thesaurus to save!")
            continue
        print(mainMenu[mainOption])

        newThesFile = FileManager.createFileFromInput("Please enter new filename: ")

        try:
            FileManager.writeToFile(newThesFile, thes)
        except Exception as e:
            UserInput.acknowledgeError(e)
        else:
            thesFile = newThesFile
            print(f'Your file "{thesFile}" has been saved')

    UserInput.anyKey()
    print()

# outside loop
print("Bye, thanks for using ST1507 DSAA: Thesaurus Based Text Processor")
