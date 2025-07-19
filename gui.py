import functions
import FreeSimpleGUI as sg


label = sg.Text("Enter your To-Do here")
input_text = sg.InputText(tooltip="Enter Todo",key="todo")
add_button = sg.Button("Add")


window = sg.Window("My To-Do App",layout=[[label],[input_text,add_button]])

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
        case sg.WIN_CLOSED:
            break



window.close()