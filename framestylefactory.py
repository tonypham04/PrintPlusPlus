from customstyle import CustomStyle
from tkinter.ttk import Frame

class FrameStyle(CustomStyle):
    
    def __init__(self, name: str, use_primary_color: bool):
        super().__init__(name)
        self.use_primary_color = use_primary_color
        self.name = f'primary{name}.{Frame().winfo_class()}' if self.use_primary_color else f'secondary{name}.{Frame().winfo_class()}'

class FrameStyleFactory:

    @staticmethod
    def get_style(name: str, use_primary_color: bool) -> FrameStyle:
        frame_style = FrameStyle(name, use_primary_color)
        if name.lower() == 'coolblue':
            FrameStyleFactory._set_styles(frame_style, 'blue' if frame_style.use_primary_color else 'lightblue')
        elif name.lower() == 'retrored':
            FrameStyleFactory._set_styles(frame_style, 'red' if frame_style.use_primary_color else 'lightyellow')
        elif name.lower() == 'cozygreen':
            FrameStyleFactory._set_styles(frame_style, 'darkseagreen' if frame_style.use_primary_color else 'floralwhite')
        return frame_style

    @staticmethod
    def _set_styles(frm_style: FrameStyle, color: str):
        frm_style.configure(frm_style.name, background = color)
