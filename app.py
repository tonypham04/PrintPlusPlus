# TODO: UI for preferences menu (palettes)
# TODO: Backend to save preferences to a JSON file
# TODO: Read preferences from JSON file
from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Text
from tkinter import filedialog
from tkinter import messagebox
from tkinter import VERTICAL
from tkinter import Menu
from idlelib.tooltip import Hovertip

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

from stylemanager import StyleManager

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

def update_palette(name: str):
    """Update the UI according to a specified style."""
    if name != None:
        StyleManager.apply_styles('button', name, button_frm)
        StyleManager.apply_styles('button', name, footer_frm)
        StyleManager.apply_styles('frame', name, frm)
        StyleManager.apply_styles('frame', name, button_frm, use_primary_color = True)
        StyleManager.apply_styles('frame', name, content_frm)
        StyleManager.apply_styles('frame', name, footer_frm, use_primary_color = True)
    else:
        StyleManager.remove_child_styles(button_frm)
        StyleManager.remove_child_styles(footer_frm)
        StyleManager.remove_widget_styles(frm)
        StyleManager.remove_widget_styles(button_frm)
        StyleManager.remove_widget_styles(content_frm)
        StyleManager.remove_widget_styles(footer_frm)
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
THEMES_ICON = '\U00002728'
PALETTE_ICON = '\U0001F3A8'
SETTINGS_ICON = '\U00002699'

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

# Tooltips
run_tooltip = Hovertip(run_btn, 'Run', 500)
reset_tooltip = Hovertip(reset_btn, 'Reset', 500)
edit_tooltip = Hovertip(edit_btn, 'Edit', 500)
quit_tooltip = Hovertip(quit_btn, 'Quit', 500)

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
# Themes menu
style = ttk.Style()
default_theme = style.theme_use()
themes_menu = Menu(menubar)
themes_sv = StringVar()
for theme in style.theme_names():
    # There is a built-in theme called 'default' but want to use 'default' to restore default theme
    if theme.lower() != 'default':
        themes_menu.add_radiobutton(label = f'{THEMES_ICON} {theme}', variable = themes_sv, command = lambda theme = theme: style.theme_use(theme))
themes_menu.add_separator()
themes_menu.add_radiobutton(label = 'Restore default..', variable = themes_sv, command = lambda: style.theme_use(default_theme))
# Palettes menu
palettes_menu = Menu(menubar)
palettes_sv = StringVar()
palettes_menu.add_radiobutton(label = f'{PALETTE_ICON} coolblue', variable = palettes_sv, command = lambda: update_palette('coolblue'))
palettes_menu.add_radiobutton(label = f'{PALETTE_ICON} retrored', variable = palettes_sv, command = lambda: update_palette('retrored'))
palettes_menu.add_radiobutton(label = f'{PALETTE_ICON} cozygreen', variable = palettes_sv, command = lambda: update_palette('cozygreen'))
palettes_menu.add_separator()
palettes_menu.add_radiobutton(label = 'Restore default..', variable = palettes_sv, command = lambda: update_palette(None))
# Preferences menu
preferences_menu = Menu(menubar)
theme_preferences = Menu(preferences_menu)
theme_preference_sv = StringVar()
for theme in style.theme_names():
    if theme.lower() != 'default':
        theme_preferences.add_radiobutton(label = f'{THEMES_ICON} {theme} (default)' if theme.lower() == default_theme.lower() else f'{THEMES_ICON} {theme}', variable = theme_preference_sv)
preferences_menu.add_cascade(menu = theme_preferences, label = f'{SETTINGS_ICON} Themes')
# Add menus to menubar
menubar.add_cascade(menu = file_menu, label = 'File')
menubar.add_cascade(menu = actions_menu, label = 'Actions')
menubar.add_cascade(menu = about_menu, label = 'About')
menubar.add_cascade(menu = themes_menu, label = 'Themes')
menubar.add_cascade(menu = palettes_menu, label = 'Palettes')
menubar.add_cascade(menu = preferences_menu, label = 'Preferences')

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
