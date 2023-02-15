import PySimpleGUI as sg
from add import Add
from development import development
from add_a_file import AddAFile


class MainStudent:
    def __init__(self) -> None:
        self.main_student = [sg.TabGroup([
                [sg.Tab("Add a student", Add().retunrn_window())],
                [sg.Tab("Add students from a file", AddAFile().return_window())],
                [sg.Tab("Student editing", [development().text()])],
                [sg.Tab("Deleting a student", [development().text()])],
                [sg.Tab("Student status", [development().text()])],
                [sg.Tab("Queries", [development().text()])],
            ])]
        
    def return_main_student(self) -> list:
        return self.main_student

