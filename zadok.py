while True:
    todo = input('Enter item (exit to exit): ')
    if todo == "exit":
        break
    file = open("todo.md", "a+")
    file.write("\n - [ ] "+todo)
    file.close()
    display = input("Do you want to display your list? (y/n) ")
    if display == "y":
        file = open("todo.md", "r")
        list = file.readlines()
        file.close()
        print(list)
