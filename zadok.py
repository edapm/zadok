import time
# define todo
todo = ""
# allow user to add to-do items
while todo != "exit":
    todo = input("Enter item ('exit' to exit): ")
    if todo != "exit":
        print("if todo != exit:")
        time.sleep(2)
        file = open("todo.md", "a+")
        print("file open")
        file.write("\n - [ ] "+todo)
        print("file write")
        time.sleep(2)
        file.close()
        print("file close")
        time.sleep(2)
        display = input("Do you want to display your list? (y/n) ")
        if display == "y":
            file = open("todo.md", "r")
            list = file.readlines()
            file.close()
            print(list)
