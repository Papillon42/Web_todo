import streamlit as st
import functions
import os

todos = functions.get_todos()

if not os.path.exists('list.txt'):
    with open('list.txt') as file:
        pass
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.out_todos(todos)

st.title('My todo')

for todo in todos:
    checkbox = st.session_state(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.out_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label='', placeholder='Enter todo', on_change=add_todo, key='new_todo')
