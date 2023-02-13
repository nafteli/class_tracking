import PySimpleGUI as sg

class MainClasses:
    def __init__(self) -> None:
        self.main_classes = [sg.TabGroup([
                [sg.Tab("Add a class", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Class editing", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Deleting a class", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
            ])]
        
    def return_main_student(self) -> list:
        return self.main_classes

