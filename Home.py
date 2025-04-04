import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase you <b>productivity<b>.",
         unsafe_allow_html=True)


st.text_input(label='New todo', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

#st.session_state