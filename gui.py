import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter your To-Do here")
input_text = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")


window = sg.Window("My To-Do App",layout=[[label],[input_text,add_button]])
window.read()
window.close()