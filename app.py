
# app.py
import functions
import FreeSimpleGUI as sg   # same API as PySimpleGUI

sg.theme("SystemDefault")

label        = sg.Text("Type in a to-do")
input_box    = sg.InputText(tooltip="Enter to-do", key="todo", do_not_clear=False)
add_button   = sg.Button("Add")
list_box     = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=(38, 10),
    expand_x=True
)
edit_button      = sg.Button("Edit")
complete_button  = sg.Button("Complete")
exit_button      = sg.Button("Exit")

window = sg.Window(
    "My To-do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box],
        [edit_button, complete_button],
        [exit_button],
    ],
    finalize=True,
)

while True:
    event, values = window.read()

    # Debug prints if you want to trace events
    # print("event:", event, "values:", values)

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    match event:
        case "Add":
            new_text = (values["todo"] or "").strip()
            if not new_text:
                sg.popup("Please type something first.", title="Nothing to add")
                continue

            todos = functions.get_todos()
            todos.append(new_text + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Edit":
            try:
                to_edit   = values["todos"][0]               # selected item (with \n)
            except (IndexError, KeyError):
                sg.popup("Please select a to-do to edit.", title="No selection")
                continue

            new_text = (values["todo"] or "").strip()
            if not new_text:
                sg.popup("Type the new text in the input box.", title="Empty edit")
                continue

            todos = functions.get_todos()
            index = todos.index(to_edit)
            todos[index] = new_text + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Complete":
            try:
                to_complete = values["todos"][0]             # selected item (with \n)
            except (IndexError, KeyError):
                sg.popup("Please select a to-do to complete.", title="No selection")
                continue

            todos = functions.get_todos()
            # Remove the exact line (with newline)
            todos.remove(to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":  # user clicked an item in the list
            try:
                selected = values["todos"][0].rstrip("\n")
                window["todo"].update(value=selected)
            except (IndexError, KeyError):
                pass

window.close()
