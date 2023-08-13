import Functions
import PySimpleGUI as sg

# Creating components for window
label = sg.Text("Add an item to you todo list:")
input_box = sg.InputText(tooltip="Enter todo item", key='todo')
add_button = sg.Button("Add")
todo_list_box = sg.Listbox(values=Functions.get_todo_list(), key='todo_items',
                           enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Creating window and displaying it
window = sg.Window('My To-Do App',
                   layout=[[label],
                   [input_box, add_button],
                   [todo_list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        # Creation of add feature
        case "Add":
            todo_list = Functions.get_todo_list()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            Functions.write_todo_list(todo_list)
            window['todo_items'].update(values=todo_list)
        # Creation of edit feature
        case "Edit":
            edit_todo = values['todo_items'][0]
            new_todo = values['todo']

            todo_list = Functions.get_todo_list()
            index = todo_list.index(edit_todo)
            todo_list[index] = new_todo
            Functions.write_todo_list(todo_list)
            window['todo_items'].update(values=todo_list)
        case "Complete":
            complete_todo = values['todo_items'][0]
            todo_list = Functions.get_todo_list()
            todo_list.remove(complete_todo)
            Functions.write_todo_list(todo_list)
            window['todo_items'].update(values=todo_list)
            window['todo'].update(value="")
        case "Exit":
            break
        case 'todo_items':
            window['todo'].update(value=values['todo_items'][0])
        case sg.WIN_CLOSED:
            break
window.close()
