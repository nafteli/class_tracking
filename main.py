
from gui.create_class import Create_class
from gui.add_student import Add_student


def main():
    class_name = Create_class().run_window_creat_class()
    Add_student().run_window_add_student(class_name)

if __name__ == '__main__':
    main()