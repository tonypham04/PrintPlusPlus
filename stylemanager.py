from tkinter.ttk import Frame
from buttonstylefactory import ButtonStyleFactory
from customstyle import CustomStyle

class StyleManager:
    @staticmethod
    def apply_styles(type: str, name: str, parent: Frame):
        if name == None:
            StyleManager.remove_styles(parent)
        elif type.lower() == 'button':
            btn_style = ButtonStyleFactory.get_style(name)
            StyleManager._set_styles(btn_style, parent)

    @staticmethod
    def _set_styles(style: CustomStyle, parent: Frame):
        for child in parent.winfo_children():
            child.configure(style = style.name)

    @staticmethod
    def remove_styles(parent: Frame):
        for child in parent.winfo_children():
            child.configure(style = child.winfo_class())

# tcl color reference: https://tcl.tk/man/tcl8.6/TkCmd/colors.htm
