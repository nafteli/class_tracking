import PySimpleGUI as sg
from student import ClassStudents, Student
from read_from_xlsx import get_data_from, seve_data


class GUI:
    def __init__(self) -> None:
        self.creat_class = [
            [sg.Text("Enter student class name: "),
             sg.InputText(key="class_name")],
            [sg.Button("Submit")]
        ]
        self.layout = [
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

    def window_creat_class(self):
        window_creat_class = sg.Window("Add class nema", self.creat_class)
        while True:
            event, values = window_creat_class.read()

            if event in (None, "Exit"):
                break

            if event == "Submit":
                class_name = ClassStudents(values["class_name"])
                window_creat_class.close()
        return class_name

    def window_layout(self, class_name):
        window_layout = sg.Window("Add Student", self.layout)
        while True:
            event, values = window_layout.read()
            if event in (None, "Exit"):
                break

            if event == 'OK':
                file_path = values["file_path"]
                dict_data = get_data_from(file_path)
                seve_data(dict_data, class_name)
                window_layout["file_path"].update("")
                window_layout["table"].update(values=class_name.get_class())

            if event == "Submit":
                student = Student(
                    values["first_name"], values["last_Name"], values["id"], values["phone"])
                student.set_student(class_name)
                window_layout["first_name"].update("")
                window_layout["last_Name"].update("")
                window_layout["id"].update("")
                window_layout["phone"].update("")
                window_layout["table"].update(values=class_name.get_class())

    def run(self):
        class_name = self.window_creat_class()
        self.window_layout(class_name)


GUI().run()
