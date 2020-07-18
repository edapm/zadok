from random import *
from time import *

todo = ""
while todo != "exit":
    todo = input("Enter item ('exit' to exit)")
    if todo != "exit":
        file = open("todo.md","a+")
        file.write("\n"+"-[ ] "+todo)
        file.close()
