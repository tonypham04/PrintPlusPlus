from tkinter import StringVar
from tkinter import Text

def update_label_text(sv: StringVar, text: str) -> None:
    sv.set(text)

def update_output_text(text: Text, content: str) -> None:
    """Replaces all text in a Text widget with new content."""
    # The Text widget must be in the 'normal' state to be edited
    current_state = text.cget('state')
    text.config(state='normal')
    text.delete("1.0", "end")
    text.insert("1.0", content)
    text.config(state=current_state)