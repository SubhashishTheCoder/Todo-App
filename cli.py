import functions
import time
now = time.strftime("%d %b ,%Y %I:%M:%S %p")
print("It is ",now)

while True:
    user_action = input("Type add, show,edit,complete or exit \n")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = functions.get_todos()

        todo = user_action[4:] + "\n"
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [ item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:

            number = int(user_action[4:].strip())

            todos = functions.get_todos()
            new_todo = input("Enter a New Todo")
            todos[number - 1] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError or IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user_action[8:].strip())
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid Input")

print("Bye")
