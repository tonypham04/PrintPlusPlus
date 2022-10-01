from customstyle import CustomStyle

class ButtonStyle(CustomStyle):
    """A CustomStyle with a name attribute which aligns with naming for a ttk.Button."""
    def __init__(self, name: str):
        super().__init__(name)
        self.name = f'{name}.TButton'

class ButtonStyleFactory:
    """Controls the instantiation of ButtonStyle objects."""
    @staticmethod
    def get_style(name: str) -> ButtonStyle:
        """Returns a ButtonStyle based on the requested palette."""
        button_style = ButtonStyle(name)
        if name.lower() == 'coolblue':
            ButtonStyleFactory._set_styles(button_style, 'blue', 'lightblue')
        elif name.lower() == 'retrored':
            ButtonStyleFactory._set_styles(button_style, 'red', 'lightyellow')
        elif name.lower() == 'cozygreen':
            ButtonStyleFactory._set_styles(button_style, 'darkseagreen', 'floralwhite')
        return button_style

    @staticmethod
    def _set_styles(btn_style: ButtonStyle, primary_color: str, secondary_color: str):
        btn_style.configure(btn_style.name, foreground = primary_color, background = secondary_color)
        btn_style.map(btn_style.name, foreground = [('active', secondary_color)], background = [('active', primary_color)])
