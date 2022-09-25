from customstyle import CustomStyle

class ButtonStyle(CustomStyle):

    def __init__(self, name: str):
        super().__init__(name)
        self.name = f'{name}.TButton'

class ButtonStyleFactory:

    @staticmethod
    def get_style(name: str):
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
