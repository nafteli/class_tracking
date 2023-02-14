import PySimpleGUI as sg
from development import development

class MainClasses:
    def __init__(self) -> None:
        self.main_classes = [sg.TabGroup([
                [sg.Tab("Add a class", [development().text()])],
                [sg.Tab("Class editing", [development().text()])],
                [sg.Tab("Deleting a class", [development().text()])],
            ])]
        
    def return_main_classes(self) -> list:
        return self.main_classes

