# import modules
from pathlib import Path
# ask user where to store todo file
path = open("PATH")
pathIs = path.readlines()
path.close()
path = str(pathIs[0].strip())
fileOpen = Path(path)
# mainloop
while True:
    # options of what to do
    choices = "1 to add item, 2 to view list, 3 to finish a todo, 4 to delete a todo, 5 to exit"
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
        with open(fileOpen, 'r') as file:
            data = file.readlines()
        print(data)
        file.close()
        todoNum = input("Which todo do you want to finish (i.e. 1, 2 etc.): ")
        todoNum = int(todoNum)
        data[todoNum] = data[todoNum].replace("- [ ]", "- [x]")
        file = open(fileOpen, 'w+')
        file.writelines(data)
        file.close()
    # option 4 -> delete todo
    elif todo == "4":
        with open(fileOpen, 'r') as file:
            data = file.readlines()
        print(data)
        file.close()
        todoNum = input("Which todo do you want to finish (i.e. 1, 2 etc.): ")
        todoNum = int(todoNum)
        data[todoNum] = data[todoNum].replace()
        file = open(fileOpen, 'w+')
        file.writelines(data)
        file.close()
    # option 5 -> exit program
    elif todo == "5":
        print("Bye!")
        break
