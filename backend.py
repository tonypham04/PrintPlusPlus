from tkinter import StringVar

def update_label_text(sv: StringVar, text: str) -> None:
    sv.set(text)