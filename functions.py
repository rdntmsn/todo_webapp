import time

FILEPATH = 'todos.txt'


def get_date_time():
    current_date_time = time.strftime("%b - %d - %Y %H:%M:%S")
    time_message = f'Today is : {current_date_time}'
    return time_message


def get_todo_items(filepath=FILEPATH):
    """ open the todos file in text format and read the lines returns the content in a list """
    with open(filepath, 'r') as f:
        todos = f.readlines()
    return todos


def write_todo_items(todo_items_arg, filepath=FILEPATH):
    """ opens the todos file in text format and writes new todo_item arguments """
    with open(filepath, 'w') as f:
        f.writelines(todo_items_arg)


if __name__ == '__main__':
    print('hello')
