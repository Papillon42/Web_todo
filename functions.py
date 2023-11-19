def get_todos():
    with open('list.txt','r') as file:
        todos = file.readlines()
        return todos

def out_todos(todos):
    with open('list.txt','w') as file:
        file.writelines(todos)