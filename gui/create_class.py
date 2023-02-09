import PySimpleGUI as sg
from methode.student_classes import ClassStudents


class Create_class:
    def __init__(self) -> None:
        self.creat_class = [
            [sg.Text("Enter student class name: "),
             sg.InputText(key="class_name")],
            [sg.Button("Submit")]
        ]


    def run_window_creat_class(self):
        window_creat_class = sg.Window("Add class nema", self.creat_class)
        while True:
            event, values = window_creat_class.read()

            if event in (None, "Exit"):
                break

            if event == "Submit":
                class_name = ClassStudents(values["class_name"])
                window_creat_class.close()
        return class_name