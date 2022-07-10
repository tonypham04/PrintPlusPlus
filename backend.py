from tkinter import StringVar
from tkinter import Text
from io import TextIOWrapper

def update_label_text(sv: StringVar, text: str) -> None:
    """Update the text in a Label widget."""
    sv.set(text)

def update_output_text(text: Text, content: str) -> None:
    """Replaces all text in a Text widget with new content."""
    # The Text widget must be in the 'normal' state to be edited
    current_state = text.cget('state')
    text.config(state='normal')
    text.delete("1.0", "end")
    text.insert("1.0", content)
    text.config(state=current_state)

def reset_output_text(text: Text) -> None:
    """Deletes all text in a Text widget."""
    current_state = text.cget('state')
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.config(state=current_state)

def export_to_file(dialog_path: TextIOWrapper, text: str) -> bool:
    """Stores the specified content in the desired file.

    Returns True on success and False otherwise."""
    if dialog_path is None or text is None:
        return False
    with open(dialog_path.name, 'w', encoding ='utf-8') as file:
        file.write(text)
    return True
