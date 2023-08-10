import Functions
import PySimpleGUI as sg

# Creating components for window
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# Creating window and displaying it
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
