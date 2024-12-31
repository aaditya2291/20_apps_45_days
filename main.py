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
# Day3
# -------------------------------------------------------------------------------#

# todos = []

# while True:
#     print("\n")
#     user_action = input("type add or show or exit ")  # takes user input
#     user_action = user_action.strip()
#     match user_action:  # match statement used to match with input
#         case "add":  # case keyword to use value based conditions
#             todo = input("enter todo: ")  # todo taking another input
#             todos.append(todo)  # appended in todo list
#             print("Next...", "\n")
#         case "show":  # case keyword to show values used in the input
#             for (
#                 element
#             ) in (
#                 todos
#             ):  # using for loop to go through the elements of the list when asked to show
#                 print(element, end=" ")

#         case "exit":  # to come out od the loop
#             break
#         case _:  # used for anything _ it can be anything
#             print(
#                 """enter only these options:
#                   1) add
#                   2) show
#                   3) exit """
#             )


# -------------------------------------------------------------------------------#
# Day4
# -------------------------------------------------------------------------------#


# todos = []

# while True:

#     user_action = input("type add or show or edit or exit ")
#     user_action = user_action.strip()
#     match user_action:
#         case "add":
#             todo = input("enter todo: ")
#             todos.append(todo)
#             print("Next...", "\n")
#         case "show":
#             for element in todos:
#                 print(element, end=" ")
#             print("\n")
#         case "edit":
#             number = int(
#                 input("enter the index number of the element you want to change")
#             )
#             number = number - 1
#             new_todo = input("enter the new todo")
#             todos[number] = new_todo
#         case "exit":
#             break
#         case _:
#             print(
#                 """enter only these options:
#                   1) add
#                   2) show
#                   3) exit """
#             )

# -------------------------------------------------------------------------------#
# Day 5
# -------------------------------------------------------------------------------#


# todos = []

# while True:

#     user_action = input("type add or show or edit or complete or exit ")
#     user_action = user_action.strip()
#     match user_action:
#         case "add":
#             todo = input("enter todo: ")
#             todos.append(todo)
#             print("Next...", "\n")
#         case "show":
#             for index, element in enumerate(todos):
#                 print(f"{index+1}) {element}", end="\n")
#             print("\n")
#         case "edit":
#             number = int(
#                 input("enter the index number of the element you want to change")
#             )
#             number = number - 1
#             new_todo = input("enter the new todo")
#             todos[number] = new_todo
#         case "complete":
#             number = int(input("enter the index number you want to remove "))
#             todos.pop(number - 1)
#         case "exit":
#             break
#         case _:
#             print(
#                 """enter only these options:
#                   1) add
#                   2) show
#                   3) exit """
#             )


# -------------------------------------------------------------------------------#
# Day 6
# -------------------------------------------------------------------------------#


# while True:

#     user_action = input("type add or show or edit or complete or exit ")
#     user_action = user_action.strip()
#     match user_action:
#         case "add":
#             todo = input("enter todo: ") + "\n"
#             file = open(
#                 "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
#                 "r",
#                 encoding="utf-8",
#             )
#             todos = file.readlines()
#             file.close()
#             todos.append(todo)
#             file = open(
#                 "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
#                 "w",
#                 encoding="utf-8",
#             )
#             file.writelines(todos)
#             print("Todo added. Next...\n")

#             print("Next...", "\n")
#             file.close()
#         case "show":
#             for index, element in enumerate(todos):
#                 print(f"{index+1}) {element}", end="\n")
#             print("\n")
#             file = open(
#                 "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
#                 "r",
#                 encoding="utf-8",
#             )
#             todos = file.readlines()
#             file.close()
#         case "edit":
#             number = int(
#                 input("enter the index number of the element you want to change")
#             )
#             number = number - 1
#             new_todo = input("enter the new todo")
#             todos[number] = new_todo
#         case "complete":
#             number = int(input("enter the index number you want to remove "))
#             todos.pop(number - 1)
#         case "exit":

#             break
#         case _:
#             print(
#                 """enter only these options:
#                   1) add 
#                   2) show
#                   3) exit """
#             )


# -------------------------------------------------------------------------------#
# Day 7
# -------------------------------------------------------------------------------#


while True:

    user_action = input("type add or show or edit or complete or exit ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter todo: ") + "\n"
            file = open(
                "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
                "r",
                encoding="utf-8",
            )
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open(
                "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
                "w",
                encoding="utf-8",
            )
            file.writelines(todos)
            print("Todo added. Next...\n")

            print("Next...", "\n")
            file.close()
        case "show":
            for index, element in enumerate(todos):
                print(f"{index+1}) {element}", end="\n")
            print("\n")
            file = open(
                "F:\\aditya_git\\20_apps_45_days\\To_do_list_app\\todo.txt",
                "r",
                encoding="utf-8",
            )
            todos = file.readlines()
            file.close()
        case "edit":
            number = int(
                input("enter the index number of the element you want to change")
            )
            number = number - 1
            new_todo = input("enter the new todo")
            todos[number] = new_todo
        case "complete":
            number = int(input("enter the index number you want to remove "))
            todos.pop(number - 1)
        case "exit":

            break
        case _:
            print(
                """enter only these options:
                  1) add 
                  2) show
                  3) exit """
            )