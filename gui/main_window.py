import PySimpleGUI as sg
from gui.students.add import Add
from students.main_student import MainStudent
from classes.main_classes import MainClasses
from development import development


class MainWindow:
    def __init__(self) -> None:
        self.navbar = [
            [sg.Tab("Day progress", [development().text()])],
            [sg.Tab("Student progress", [development().text()])],
            [sg.Tab("Management", [development().text()])],
            [sg.Tab("Courses", [development().text()])],
            [sg.Tab("Students", [MainStudent().return_main_student()])],
            [sg.Tab("Classes", [MainClasses().return_main_classes()])],
        ]
        self.main_window = [[sg.TabGroup(self.navbar)]]

    def run_main_window(self):
        window_main_window = sg.Window("Main Window", self.main_window)
        while True:
            event, values = window_main_window.read()
            if event in (None, "Exit"):
                break
            elif event:
                add_studenst = Add().run_window(window_main_window, event, values)
                if not add_studenst:
                    development().popup()
        window_main_window.close()
