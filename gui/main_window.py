import PySimpleGUI as sg
from students.main_student import MainStudent


class MainWindow:
    def __init__(self) -> None:
        self.navbar = [
                [sg.Tab("Day progress", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Student progress", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Management", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Courses", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
                [sg.Tab("Students", [MainStudent().return_main_student()])],
                [sg.Tab("Classes", [[sg.Text("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")]])],
            ]
        self.main_window = [[sg.TabGroup(self.navbar)]]

    def run_main_window(self):
        window_main_window = sg.Window("Main Window", self.main_window)
        while True:
            event, values = window_main_window.read()
            if event in (None, "Exit"):
                break
            elif event:
                sg.popup("⚒️⚒️⚒️ Feature under development ⚒️⚒️⚒️")
        window_main_window.close()

# MainWindow().run_main_window()
