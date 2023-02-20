from student import Student


class Students:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Students, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.add_student = []

    def creat_studend(
        self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None
    ):
        student = Student(first_name, last_Name, id, phone, classID)
        self.add_student.append(student)
        return self.add_student

    def get_students(self) -> list:
        return self.add_student


add = Students()
