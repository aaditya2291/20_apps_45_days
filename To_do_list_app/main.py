"""to-do-app"""

# ______________________________________________________________________________#
# day2
# ______________________________________________________________________________#
# Message = "Enter a todo:"
# todo1 = input(Message)
# print(todo1)
# todo2 = input(Message)
# print(todo2)
# todo3 = input(Message)
# print(todo3)

# todos = [todo1, todo2, todo3]
# print(todos, "\n")

# todo_list = []

# while True:
#     todo3 = input(Message)
#     todo_list.append(todo3)
#     print("Next....", "\n")
#     print(todo_list, "\n")

# -------------------------------------------------------------------------------#
# day3
# -------------------------------------------------------------------------------#

todos = []

while True:
    user_action = input("type add or show ")

    match user_action:
        case "add":
            todo = input("enter todo: ")
            todos.append(todo)
            print("Next...", "\n")
        case "show":
            print(todos, "\n")
