import PySimpleGUI as sg
from methode.student import Student


class Add:
    def __init__(self) -> None:
        self.add = [
            [sg.Text("Enter student first_name: "), sg.InputText(key="first_name")],
            [sg.Text("Enter student last_Name: "), sg.InputText(key="last_Name")],
            [sg.Text("Enter student id: "), sg.InputText(key="id")],
            [sg.Text("Enter student phone: "), sg.InputText(key="phone")],
            [sg.Text("Enter student class: "), sg.InputText(key="class")],
            [sg.Button("Submit")],
        ]

    def retunrn_window(self):
        return self.add

    def run_window(self, window_main_window, event, values):
        if event == "Submit":
                student = Student(
                    values["first_name"], values["last_Name"], values["id"], values["phone"])
                window_main_window["first_name"].update("")
                window_main_window["last_Name"].update("")
                window_main_window["id"].update("")
                window_main_window["phone"].update("")
                print(student.__str__())
                return True
        return False