def get_todos():
    """ Reads a text file and returns a list or to-do items """
    with open('todos.txt', 'r') as file_local:  # Context manager
        todos_local = file_local.readlines()
    return todos_local

def write_todos(arg_todos):
    """ Writes the to-do items list in the text file """
    with open('todos.txt', 'w') as file_local:  # Context manager
        file_local.writelines(arg_todos)
                                                # This function doesn't return anything. So, no return value added

if __name__ == '__main__':
    print("Hello")          # This part of the code will not be executed during execution of main14.py file