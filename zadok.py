# define todo
todo = ""
# allow user to add to-do items
while todo != "exit":
    todo = input("Enter item ('exit' to exit): ")
    if todo != "exit":
        file = open("todo.md", "a+")
        file.write("\n- [ ] "+todo)
        display = input("Do you want to display your list? (y/n) ")
        if display == "y":
            list = file.readlines()
            file.close()
            print(list)
        else:
            file.close()
