from tkinter.ttk import Style

class CustomStyle(Style):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
