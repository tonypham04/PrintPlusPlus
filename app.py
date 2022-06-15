from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Text

from backend import update_output_text
from backend import reset_output_text

# Create the main window of the application
root = Tk()
root.title('Button Config Options')
root.minsize(300, 100)
# Built-in options: error, gray25, gray50, hourglass, info, questhead, question, warning
root.iconbitmap('hourglass')

# Create widgets
frm = ttk.Frame(root, padding=10)

button_frm = ttk.Frame(frm, padding=10)
run_btn = ttk.Button(button_frm, text='Run', command=lambda: update_output_text(output_text, str(run_btn.configure().keys())))
reset_btn = ttk.Button(button_frm, text='Reset', command=lambda: reset_output_text(output_text))

content_frm = ttk.Frame(frm, padding=10)
results_txt = StringVar()
# output_lbl = ttk.Label(content_frm, textvariable=results_txt)
output_text = Text(content_frm, state='disabled', wrap='word', bg='#D3D3D3')

footer_frm = ttk.Frame(frm, padding=10)
quit_btn = ttk.Button(footer_frm, text='Quit', command=root.destroy)

# Place widgets
frm.grid()

button_frm.grid(row=0, column=0, sticky='w')
run_btn.grid(row=0, column=0)
reset_btn.grid(row=0, column=1, padx=10)

content_frm.grid(row=1, column=0)
output_text.grid(row=1, column=0)

footer_frm.grid(row=2, column=0)
quit_btn.grid(row=0, column=0)

root.mainloop()

#TODO: http://tkdocs.com/tutorial/index.html