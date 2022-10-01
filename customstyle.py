from tkinter.ttk import Style

class CustomStyle(Style):
    """Wrapper class to ttk.Style which includes a name attribute."""
    def __init__(self, name: str):
        super().__init__()
        self.name = name
