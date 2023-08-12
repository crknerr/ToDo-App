import Functions
import PySimpleGUI as sg

# Creating components for window
label = sg.Text("Add an item to you todo list:")
input_box = sg.InputText(tooltip="Enter todo item", key="todo")
add_button = sg.Button("Add")

# Creating window and displaying it
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = Functions.get_todo_list()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            Functions.write_todo_list(todo_list)
        case sg.WIN_CLOSED:
            break
window.close()
