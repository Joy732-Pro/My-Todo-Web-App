import streamlit as st
import functions

# st.set_page_config(layout="wide")       # allows to set page configurations

todos = functions.get_todos()       # It is better to define todos before the add_todo() function
def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"      # takes the new string from the St.input_text(key="new_todo")
    todos.append(todo1)
    functions.write_todos(todos)

st.title("My todo App")
st.subheader("This is a Web-App")
st.write("This app is to increase your <b>productivity</b>",
         unsafe_allow_html=True)            # "unsafe_allow_html=True" enables the usage of html tags  | HTML is only allowed for write method
# St.checkbox("Buy grocery.")

for index, todo in enumerate(todos):
   checkbox = st.checkbox(todo, key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()           # Whenever a box is checked, it reruns the loop, so the shown list is being updated instantly

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")