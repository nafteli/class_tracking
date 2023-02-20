
import test_import_paths
from methode.add_students_file import ReadFile, SetStudents
from methode.student import Student
from gui.main_window import MainWindow


def main():
    # local = Student()
    w = Student('a', 'b', 1, 2)
    w = Student('aגהבה', 'bבההג', 1, 2)
    a = ReadFile('/home/evyatar/PycharmProjects/class_tracking/files/כיתה 5 ירושלים.xlsx').get_data_from()
    b = SetStudents(a).seve_data()
    w = Student('a', 'b', 1, 2)
    w = Student('a', 'b', 1, 2)
    s = Student.get_all_students()
    print('s', s)
    MainWindow().run_main_window()

if __name__ == '__main__':
    main()