# import modules
from pathlib import Path
# ask user where to store todo file
fileOpen = Path(input("Enter file path (see docs for more info): "))
# mainloop
while True:
    # options of what to do
    choices = "1 to add item, 2 to view list, 3 to finish a todo, 4 to exit"
    print(choices)
    todo = input("Enter choice (1-4): ")
    # option 1 -> add item
    if todo == "1":
        file = open(fileOpen, "a+")
        text = input("Enter item: ")
        file.write("\n - [ ] " + text)
        file.close()
    # option 2 -> read list
    elif todo == "2":
        file = open(fileOpen, "r+")
        list = file.readlines()
        file.close()
        print(list)
    # option 3 -> finish a todo
    elif todo == "3":
        file = open(fileOpen, "a+")
    # option 4 -> exit program
    elif todo == "4":
        print("Bye!")
        break
