FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list in the text files."""
    with open(filepath, "w") as file:
            file.writelines(todos_arg)

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    meters = round(meters, 2)
    return meters

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())