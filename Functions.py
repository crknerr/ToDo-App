FILEPATH = "todo_list.txt"

def get_todo_list(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_list(todo_list_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_list_arg)