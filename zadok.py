from pathlib import Path
fileOpen = Path(input("Enter file path (see docs for more info): "))
while True:
    choices = "1 to add item, 2 to view list, 3 to exit"
    print(choices)
    todo = input("Enter choice (1-3): ")
    if todo == "1":
        file = open(fileOpen, "a+")
        text = input("Enter item: ")
        file.write("\n - [ ] " + text)
        file.close()
    elif todo == "2":
        file = open(fileOpen, "r")
        list = file.readlines()
        file.close()
        print(list)
    if todo == "3":
        print("Bye!")
        break
