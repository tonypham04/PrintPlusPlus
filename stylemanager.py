from tkinter.ttk import Frame
from buttonstylefactory import ButtonStyleFactory
from customstyle import CustomStyle
from framestylefactory import FrameStyleFactory
from tkinter.ttk import Widget

class StyleManager:
    @staticmethod
    def apply_styles(type: str, name: str, parent: Frame, use_primary_color = False):
        if type.lower() == 'button':
            btn_style = ButtonStyleFactory.get_style(name)
            StyleManager._set_styles(btn_style, parent)
        elif type.lower() == 'frame':
            frm_style = FrameStyleFactory.get_style(name, use_primary_color)
            parent.configure(style = frm_style.name)

    @staticmethod
    def _set_styles(style: CustomStyle, parent: Frame):
        for child in parent.winfo_children():
            child.configure(style = style.name)

    @staticmethod
    def remove_child_styles(parent: Frame):
        for child in parent.winfo_children():
            StyleManager.remove_widget_styles(child)

    @staticmethod
    def remove_widget_styles(widget: Widget):
        widget.configure(style = widget.winfo_class())

# tcl color reference: https://tcl.tk/man/tcl8.6/TkCmd/colors.htm
