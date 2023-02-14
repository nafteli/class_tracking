import PySimpleGUI as sg

class development:
    def __init__(self) -> None:
        self.str = "\n ⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️ \n"

    def text(self):
        return [sg.Text(self.str)]
    
    def popup(self):
        return sg.popup(self.str)