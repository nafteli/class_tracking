import PySimpleGUI as sg
# from gui.development import development


class Student:
    def __init__(self, list_students) -> None:
        self.studend = []
        for i in range(len(list_students)):
            self.studend.append([sg.Text(list_students[i][0]), sg.Text(list_students[i][1])])

    def return_window(self):
        return self.studend


class ListStudents:
    def __init__(self, list_students) -> None:
        self.list_students = [list(Student().return_window()) for _ in range(len(list_students))]
        print(self.list_students)

    def return_window(self):
        return self.list_students

