import streamlit as st
import functions


todos = functions.get_todo_items()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todo_items(todos)
    st.session_state["new_todo"] = ""


st.title('My Todo App')
st.subheader('This is a Todo App')
st.write('A webapp version of the Gui Todo App')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo_items(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New Todos", label_visibility='hidden', placeholder="Type your new todo item here",
              on_change=add_todo, key="new_todo")
