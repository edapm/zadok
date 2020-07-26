while True:
    location = ""
    choices = ["1 to change storage location", "2 to add item", "3 to view list", "4 to exit"]
    print(choices)
    todo = input("Enter choice (1-4): ")
    if todo == "1":
        location = input("Enter file location (First time using? See docs for more info): ")
    elif todo == "2":
        file = open(location + "todo.md", "a+")
        text = input("Enter item: ")
        file.write("\n - [ ] " + text)
        file.close()
    elif todo == "3":
        file = open(location + "todo.md", "r")
        list = file.readlines()
        file.close()
        print(list)
    if todo == "4":
        print("Bye!")
        break
