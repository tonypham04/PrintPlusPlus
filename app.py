from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Text
from tkinter import filedialog
from tkinter import messagebox
from tkinter import VERTICAL

from backend import run_function
from backend import reset_function
from backend import export_to_file
from backend import make_text_editable

from io import TextIOWrapper

from service import run

def open_export_prompt() -> TextIOWrapper:
    """Open a file dialog and prompt user for path if there is content to export.

    Display a message box otherwise."""
    return filedialog.asksaveasfile(filetypes = [('Text files', '.txt')], defaultextension = '.txt', initialfile = 'data')

def try_export() -> None:
    """Attempt to export data if there is any and show message of successful export.

    Show an error dialog otherwise."""
    data = output_text.get('1.0', 'end')
    if not data.isspace():
        file_path = open_export_prompt()
        if export_to_file(file_path, data):
            messagebox.showinfo(title = 'Export Success \U00002705', message = f'Successfully exported {file_path.name} ' + '\U0001F913')
    else:
        messagebox.showerror(message = 'There is nothing to export. \U0001F641', title = 'Export Error \U0000274E')

# Constants
READONLY_COLOR = '#D3D3D3'

# Create the main window of the application
root = Tk()
root.title('Print++')
root.minsize(300, 100)
# Built-in options: error, gray25, gray50, hourglass, info, questhead, question, warning
root.iconbitmap('hourglass')
root.resizable(False, False)

# Create widgets
frm = ttk.Frame(root, padding = 10)

button_frm = ttk.Frame(frm, padding = 10)
run_btn = ttk.Button(button_frm, text = '\U00002BC8 Run', command = lambda: run_function(output_text, run(run_btn.configure().keys()), READONLY_COLOR))
reset_btn = ttk.Button(button_frm, text = '\U0001F5D8 Reset', command = lambda: reset_function(output_text, READONLY_COLOR))
export_btn = ttk.Button(button_frm, text = '\U0001F4BE Export', command = lambda: try_export())
edit_btn = ttk.Button(button_frm, text = '\U0001F589 Edit', command = lambda: make_text_editable(output_text, '#dbe9f4'))

content_frm = ttk.Frame(frm, padding=10)
results_txt = StringVar()
output_text = Text(content_frm, state = 'disabled', wrap = 'word', bg = READONLY_COLOR)
scrollbar = ttk.Scrollbar(content_frm, orient = VERTICAL, command = output_text.yview)
output_text.configure(yscrollcommand = scrollbar.set)

footer_frm = ttk.Frame(frm, padding = 10)
quit_btn = ttk.Button(footer_frm, text = 'Quit', command = root.destroy)

# Place widgets
frm.grid()

button_frm.grid(row = 0, column = 0, sticky = 'w')
run_btn.grid(row = 0, column = 0)
reset_btn.grid(row = 0, column = 1, padx = 10)
export_btn.grid(row = 0, column = 2)
edit_btn.grid(row = 0, column = 3, padx = 10)

content_frm.grid(row = 1, column = 0)
output_text.grid(row = 1, column = 0)
scrollbar.grid(row = 1, column = 1, sticky = 'ns')

footer_frm.grid(row = 2, column = 0)
quit_btn.grid(row = 0, column = 0)

root.mainloop()

#TODO: http://tkdocs.com/tutorial/index.html
