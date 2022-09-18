from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Text
from tkinter import filedialog
from tkinter import messagebox
from tkinter import VERTICAL
from tkinter import Menu

from backend import run_function
from backend import reset_function
from backend import export_to_file
from backend import make_text_editable
from backend import save_and_close
from backend import update_output_text
from backend import get_initial_text
from backend import append_text_from_file

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
BACKUP_FILENAME = 'temp.txt'
# Icons
RUN_ICON = '\U00002BC8'
RESET_ICON = '\U0001F5D8'
EXPORT_ICON = '\U0001F4BE'
EDIT_ICON = '\U0001F589'
BOOK_ICON = '\U0001F4D6'
QUIT_ICON = '\U0000274C'

# Create the main window of the application
root = Tk()
root.title('Print++')
root.minsize(300, 100)
# Built-in options: error, gray25, gray50, hourglass, info, questhead, question, warning
root.iconbitmap('hourglass')
root.resizable(False, False)
# Remove dashed line from menu
root.option_add('*tearOff', False)

# Create widgets
frm = ttk.Frame(root, padding = 10)

button_frm = ttk.Frame(frm, padding = 10)
run_btn = ttk.Button(button_frm, text = RUN_ICON, command = lambda: run_function(output_text, run(run_btn.configure().keys()), READONLY_COLOR))
reset_btn = ttk.Button(button_frm, text = RESET_ICON, command = lambda: reset_function(output_text, READONLY_COLOR))
edit_btn = ttk.Button(button_frm, text = EDIT_ICON, command = lambda: make_text_editable(output_text, '#dbe9f4'))

content_frm = ttk.Frame(frm, padding=10)
results_txt = StringVar()
output_text = Text(content_frm, state = 'disabled', wrap = 'word', bg = READONLY_COLOR)
scrollbar = ttk.Scrollbar(content_frm, orient = VERTICAL, command = output_text.yview)
output_text.configure(yscrollcommand = scrollbar.set)

footer_frm = ttk.Frame(frm, padding = 10)
quit_btn = ttk.Button(footer_frm, text = QUIT_ICON, command = lambda: save_and_close(BACKUP_FILENAME, output_text.get('1.0', 'end'), root))

# Initial Setup
update_output_text(output_text, get_initial_text(BACKUP_FILENAME))

# Create menubar
menubar = Menu(root)
# File menu
file_menu = Menu(menubar)
file_menu.add_command(label = '\u2795 Add text from file..', command = lambda: append_text_from_file(output_text, filedialog.askopenfile(filetypes = [('Text files', '.txt')])))
file_menu.add_command(label = f'{EXPORT_ICON} Export to text file..', command = try_export)
file_menu.add_separator()
file_menu.add_command(label = f'{QUIT_ICON} Quit', command = quit_btn.invoke)
# Actions menu
actions_menu = Menu(menubar)
actions_menu.add_command(label = f'{RUN_ICON} Run', command = run_btn.invoke)
actions_menu.add_command(label = f'{RESET_ICON} Reset', command = reset_btn.invoke)
actions_menu.add_command(label = f'{EDIT_ICON} Edit', command = edit_btn.invoke)
# About menu
about_menu = Menu(menubar)
about_menu.add_command(label = f'{BOOK_ICON} Run function..', command = lambda: messagebox.showinfo(title = 'Run function documentation', message = run_function.__doc__))
about_menu.add_command(label = f'{BOOK_ICON} Reset function..', command = lambda: messagebox.showinfo(title = 'Reset function documentation', message = reset_function.__doc__))
about_menu.add_command(label = f'{BOOK_ICON} Edit function..', command = lambda: messagebox.showinfo(title = 'Edit function documentation', message = make_text_editable.__doc__))
about_menu.add_separator()
about_menu.add_command(label = f'{BOOK_ICON} Adding text from file..', command = lambda: messagebox.showinfo(title = 'Adding text from file documentation', message = append_text_from_file.__doc__))
about_menu.add_command(label = f'{BOOK_ICON} Export to text file..', command = lambda: messagebox.showinfo(title = 'Export function documentation', message = try_export.__doc__))
about_menu.add_separator()
about_menu.add_command(label = f'{BOOK_ICON} Quit function..', command = lambda: messagebox.showinfo(title = 'Quit function documentation', message = save_and_close.__doc__))
# Add menus to menubar
menubar.add_cascade(menu = file_menu, label = 'File')
menubar.add_cascade(menu = actions_menu, label = 'Actions')
menubar.add_cascade(menu = about_menu, label = 'About')

# Place widgets
root.configure(menu = menubar)
frm.grid()

button_frm.grid(row = 0, column = 0, sticky = 'w')
run_btn.grid(row = 0, column = 0)
reset_btn.grid(row = 0, column = 1, padx = 10)
edit_btn.grid(row = 0, column = 2)

content_frm.grid(row = 1, column = 0)
output_text.grid(row = 1, column = 0)
scrollbar.grid(row = 1, column = 1, sticky = 'ns')

footer_frm.grid(row = 2, column = 0)
quit_btn.grid(row = 0, column = 0)

# Event bindings
root.bind('<Escape>', lambda e: quit_btn.invoke())
root.protocol('WM_DELETE_WINDOW', quit_btn.invoke)

root.mainloop()
