import PySimpleGUI as sg
from methode.student_classes import Student
from methode.read_from_xlsx import get_data_from, seve_data


class Add_student:
    def __init__(self) -> None:
        self.add_student = [
                [sg.TabGroup([[sg.Tab('add student',
                                    [[sg.Text("Enter student first_name: "),
                                        sg.InputText(key="first_name")],
                                        [sg.Text("Enter student last_Name: "),
                                        sg.InputText(key="last_Name")],
                                        [sg.Text("Enter student id: "),
                                        sg.InputText(key="id")],
                                        [sg.Text("Enter student phone: "),
                                        sg.InputText(key="phone")],
                                        [sg.Button("Submit")],]),
                            sg.Tab('add file student', [
                                [sg.Text('Select a file:')], [sg.Input(key="file_path"), sg.FileBrowse()], [sg.OK(), sg.Cancel()],])]])],
                [sg.Table(values=[], headings=["First name", "Last Name", "Id", "Phone"], max_col_width=25, auto_size_columns=False,
                        display_row_numbers=False, alternating_row_color='lightblue', key='table', def_col_width=12)]
            ]
        
    
    def run_window_add_student(self, class_name):
        window_add_student = sg.Window("Add Student", self.add_student)
        while True:
            event, values = window_add_student.read()
            if event in (None, "Exit"):
                break

            if event == 'OK':
                file_path = values["file_path"]
                dict_data = get_data_from(file_path)
                seve_data(dict_data, class_name)
                window_add_student["file_path"].update("")
                window_add_student["table"].update(values=class_name.get_class())

            if event == "Submit":
                student = Student(
                    values["first_name"], values["last_Name"], values["id"], values["phone"])
                student.set_student(class_name)
                window_add_student["first_name"].update("")
                window_add_student["last_Name"].update("")
                window_add_student["id"].update("")
                window_add_student["phone"].update("")
                window_add_student["table"].update(values=class_name.get_class())
