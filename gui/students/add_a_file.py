import PySimpleGUI as sg
from methode.add_students_file import ReadFile, SetStudents


class AddAFile:
    def __init__(self) -> None:
        self.add_a_file = [
            [sg.Text("Select a file:")],
            [sg.Input(key="file_path"), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()],
        ]

    def return_window(self):
        return self.add_a_file

    def run_window(self, window_main_window, event, values):
        if event == "OK":
            data_file = ReadFile(values["file_path"]).get_data_from()
            SetStudents(data_file).seve_data()
            window_main_window["file_path"].update("")
            return True
        if event == "Cancel":
            window_main_window["file_path"].update("")
            return True
        return False
