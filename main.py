import time as t
import os

# Finds out what batshit crazy folder the program is contained in
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
finfolder = os.listdir()

def main():

    # Main command prompt kinda thing, I guess.
    def commandPrompt():
        print("Command Prompt V1")
        cmd = input(": ")
        if cmd == "-t":
            print(THIS_FOLDER)
        if cmd == "-ls":
            print(finfolder)
        if cmd == "home":
            mainMenu()   
        main()

    # Notepad but with more options dickwad
    def improvedNotepad():
        print("--------------")
        print("Better Notepad")
        print("--------------")
        print()
        holder1 = input("Enter file name (Including file extension): ")
        print()
        print("Options: Append ")
        print("         Create")
        input2 = input("Enter what you would like to do: ")
        if input2 == "append":
            holder2 = "a"
        if input2 == "Append":
            holder2 = "a"
        if input2 == "create":
            holder2 = "w+"
        if input2 == "Create":
            holder2 = "w+"
        f = open(holder1, holder2)
        input1 = input(": ")
        f.write(input1)
        f.close()

        mainMenu()

    # Why is this shit not fucking working? Am I retarded? Like medically?
    def fileReader():
        print("------------------")
        print(".txt File Reader")
        print("------------------")
        openfilename1 = input("Enter file name: ")
        openfilename2 = os.path.join(THIS_FOLDER, openfilename1)
        switch1 = os.path.isfile(openfilename2)
        if switch1 == True:
            f = open(openfilename2, "r")
            contents1 = f.read()
            print()
            print(contents1)
            t.sleep(2)
            print()
            input("Press enter to continue...")
            print()
            mainMenu()
        if switch1 == False:
            print()
            print("File does not exist")
            print()
            input("Press enter to continue...")
            print()
            mainMenu()
        mainMenu()

    # Shit was worked on and now works, smartass
    def notepad():
        print("---------")
        print("Notepad")
        print("---------")
        filename1 = str(input("Enter file name: "))
        f = open(filename1 + ".txt", "w+")
        padcontents = str(input(": "))
        f.write(padcontents)
        f.close()

        mainMenu()

    # This shit is basically just a calculator
    def calculator():
        print("-----------")
        print("Calculator")
        print("-----------")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op1 = str(input("Enter the operation: "))

        if op1 == "+":
            ans1 = (num1 + num2)
            print(ans1)
        if op1 == "-":
            ans1 = (num1 - num2)
            print(ans1)
        if op1 == "*":
            ans1 = (num1 * num2)
            print(ans1)
        if op1 == "/":
            ans1 = (num1 / num2)
            print(ans1)

        mainMenu()

    # Main Menu shit, needs to be continuously updated
    def mainMenu():
        print("-----------")
        print("Main Menu:")
        print("----------")
        print("1. Calculator")
        print("2. Notepad")
        print("3. File reader")
        print("4. Improved Notepad")
        print("5. CMD")

        option1 = input(": ")

        if option1 == "calc":
            calculator()
        elif option1 == "Calculator":
            calculator()
        elif option1 == "calculator":
            calculator()
        elif option1 == "!1":
            calculator()
        elif option1 == "!2":
            notepad()
        elif option1 == "notepad":
            notepad()
        elif option1 == "Notepad":
            notepad()
        elif option1 == "!3":
            fileReader()
        elif option1 == "File reader":
            fileReader()
        elif option1 == "file reader":
            fileReader()
        elif option1 == "listdir":
            files = os.listdir()
            print(files)
        elif option1 == "!4":
            improvedNotepad()
        elif option1 == "Imporved Notepad":
            improvedNotepad()
        elif option1 == "cmd":    
            commandPrompt()
        elif option1 == "CMD":
            commandPrompt()
        else:
            print("Unknown command\n")    
            mainMenu()
    mainMenu()


main()
