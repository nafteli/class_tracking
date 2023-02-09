import pandas as pd
# from student import ClassStudents, Student
from methode.student_classes import ClassStudents, Student


def get_data_from(excel_file):
    df = pd.read_excel(excel_file)
    return [list(row) for index, row in df.iterrows()]

def seve_data(dict_data, class_name):
    print(dict_data)
    for index in range(len(dict_data)):
        student = Student(dict_data[index][0][::-1], dict_data[index][1][::-1], dict_data[index][2], dict_data[index][3])
        student.set_student(class_name)
