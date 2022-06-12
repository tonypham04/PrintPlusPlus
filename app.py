from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

from backend import update_label_text

# Create the main window of the application
root = Tk()
root.title('Button Config Options')
root.minsize(300, 100)
# Built-in options: error, gray25, gray50, hourglass, info, questhead, question, warning
root.iconbitmap('hourglass')

# Create widgets
frm = ttk.Frame(root, padding=10)

content_frm = ttk.Frame(frm, padding=10)
results_txt = StringVar()
output_lbl = ttk.Label(content_frm, textvariable=results_txt)
run_btn = ttk.Button(content_frm, text='Run', command=lambda: update_label_text(results_txt, str(run_btn.configure().keys())))

footer_frm = ttk.Frame(frm, padding=10)
quit_btn = ttk.Button(footer_frm, text='Quit', command=root.destroy)

# Place widgets
frm.grid()

content_frm.grid(row=0, column=0)
run_btn.grid(row=0, column=0)
output_lbl.grid(row=1, column=0)

footer_frm.grid(row=1, column=0)
quit_btn.grid(row=0, column=0)

root.mainloop()

#TODO: https://docs.python.org/3/library/tkinter.html#important-tk-concepts