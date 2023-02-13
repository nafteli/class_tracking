import PySimpleGUI as sg

# import pandas as pd

students_dict = {
    0: {"id":0},
    1: {
        "first_name": "naftali",
        "last_name": "zeivald",
        "id": 209329994,
        "phone": "053-7225919",
        "email": "naftali2055@gmail.com",
    },
    2: {
        "first_name": "bla",
        "last_name": "alb",
        "id": 48486,
        "phone": "050-1234567",
    },
    3: {
        "first_name": "na",
        "last_name": "zeiv",
        "id": 4886,
        "phone": "053-7225919",
    },
    4: {
        "first_name": "naftali",
        "last_name": "zeivald",
        "id": 486,
        "phone": "053-7225919",
        "email": "naftali@gmail.com",
    },
    5: {
        "first_name": "naftali",
        "last_name": "zeivald",
        "id": 4848634567,
        "phone": "053-7225919",
        "email": "naftali@gmail.com",
    },
}
# df = pd.DataFrame(students_dict.values())
# df.set_index('id', inplace=True, drop=False)
# print(df.loc[4886])
# print(df[df.phone.str.startswith("053")].index)


def Student(id=0):
    # for st in students_dict.values():
    #     print(type(st), st.get("id"))
    return [stodent for stodent in students_dict.values() if stodent["id"] == id][0]


studentID = 4886
student = Student(studentID)
layout = [
    [
        sg.Column([sg.Text(key if key else "")] for key in student.keys()),
        sg.Column(
            [sg.InputText(value if value else "", readonly=True)]
            for value in student.values()
        ),
    ],
    [sg.Cancel(), sg.Button(key="Edit", button_text="Edit")],
]
first_name = student.get("first_name")
last_name = student.get("last_name")
Window = sg.Window(f"{first_name if first_name else ''} {last_name if last_name else ''}", layout)
event, values = Window.read()
print(event, values)
Window.close()


class ShowStudent:
    def __init__(self) -> None:
        self.show_student = [
            [
                sg.Column([sg.Text(key if key else "")] for key in Student(id).keys()),
                sg.Column(
                    [sg.Text(value if value else "")] for value in Student(id).values()
                ),
            ],
            [sg.Cancel()],
        ]
        self.id = id

    def run_window_show_student(self, id):
        first_name = Student(id).get("first_name")
        last_name = Student(id).get("last_name")
        while True:
            Window = sg.Window(f"{first_name} {last_name}", layout)
            event, values = Window.read()
