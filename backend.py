from tkinter import Tk
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

def append_output_text(text: Text, content: str, separator = '\n') -> None:
    """Appends text to a Text widget."""
    if is_empty_text(text):
        separator = ''
    current_state = text.cget('state')
    text.config(state = 'normal')
    text.insert("end", f'{separator}{content}')
    text.config(state = current_state)

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

def make_text_editable(text: Text, bg_color: str) -> None:
    """Make a Text widget editable with a visual indicator to show it is editable."""
    text.config(state = 'normal')
    text.config(bg = bg_color)

def make_text_readonly(text: Text, disabled_color: str) -> None:
    """Make a Text widget readonly with a visual indicator to show it is not editable."""
    text.config(state = 'disabled')
    text.config(bg = disabled_color)

def run_function(text: Text, content: str, disabled_color: str) -> None:
    """Append output to a Text widget and make it readonly."""
    append_output_text(text, content)
    make_text_readonly(text, disabled_color)

def reset_function(text: Text, disabled_color: str) -> None:
    """Clears all contents in a Text widget and makes it readonly."""
    reset_output_text(text)
    make_text_readonly(text, disabled_color)

def is_empty_text(text: Text) -> bool:
    """Checks whether a Text widget has no content.

    Returns true if the Text is empty and false otherwise."""
    return text.get('1.0', 'end').isspace()

def save_text(filename: str, text: str) -> None:
    """Saves text to a file."""
    with open(f'./{filename}', 'w', encoding = 'utf-8') as file:
        file.write(text)

def save_and_close(filename: str, text: str, root: Tk):
    """Saves text to a file and close the application."""
    save_text(filename, text)
    root.destroy()

def get_initial_text(filename: str) -> str:
    """Returns the string contents from a backup file."""
    try:
        with open(f'./{filename}', 'r', encoding = 'utf-8') as file:
            initial_text = file.read()
    except FileNotFoundError:
        initial_text = ''
    return initial_text

# Menubar functions
def get_text_from_file(file_path: str) -> str:
    """Returns the text content from a file."""
    with open(file_path, 'r', encoding = 'utf-8') as file:
        return file.read()

def append_text_from_file(text: Text, file_path: TextIOWrapper, separator = '\n') -> None:
    """Appends text from a text file to a Text widget."""
    if file_path is None:
        return
    file_text = get_text_from_file(file_path.name)
    append_output_text(text, file_text, separator)
