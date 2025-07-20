import functions
import FreeSimpleGUI as sg


label = sg.Text("Enter your To-Do here")
input_text = sg.InputText(tooltip="Enter Todo",key="todo")
add_button = sg.Button("Add")
list_todos = sg.Listbox(values=functions.get_todos(),
                        enable_events=True,
                        size=(45,10),
                        key="todos")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_text,add_button],
                           [list_todos,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            list_todos.update(values=todos)
        case "Edit" :
            todo_to_edit = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = values['todo']
            functions.write_todos(todos)
            list_todos.update(values=todos)
        case "Complete":
            todos = functions.get_todos()
            todo_to_complete = values['todos'][0]
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            list_todos.update(values = todos)
            input_text.update(value="")
        case "todos":
           input_text.update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break



window.close()