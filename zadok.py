# define todo
todo = ""
# allow user to add to-do items
while todo != "exit":
    todo = input("Enter item ('exit' to exit): ")
    if todo != "exit":
        file = open("todo.md", "a+")
        file.write("\n- [ ] "+todo)
        file.close()
