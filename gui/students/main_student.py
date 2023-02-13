import PySimpleGUI as sg

class MainStudent:
    def __init__(self) -> None:
        self.main_student = [sg.TabGroup([
                [sg.Tab("Add a student", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Student editing", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Deleting a student", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Student status", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Queries", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
            ])]
        
    def return_main_student(self) -> list:
        return self.main_student

