

class ClassStudents():
    """
    Class for holding information about a group of students in a class.

    Attributes:
        __class_first_name (str): The first_name of the class.
        __student_storage (dict): A dictionary that stores all students in the class. The key is the student's id and the
            value is the `Student` instance.
    
    """

    def __init__(self, class_name: str) -> None:
        """
        Args:
            class_name (str): The name of the class.
        
        """
        self.__class_name = class_name
        self.__student_storage = {}

    def add_student(self, student: "Student"):
        """
        Adds a student to the class.

        Args:
            student (Student): An instance of the `Student` class.

        """
        self.__student_storage[len(self.__student_storage)] = student

    def get_class(self) -> list:
        """
        Returns:
            dict: A dictionary that maps the student's id to their information.
        
        """
        return [student.get_student() for id, student in self.__student_storage.items()]

    def get_student(self, student_id: int) -> dict:
        """
        Retrieves a student's information by their id.

        Args:
            student_id (int): The id of the student to retrieve.

        Returns:
            dict: The student's information.
        
        """
        return self.__student_storage[student_id].get_student()


class Student:
    """
    Class for holding information about a student.

    Attributes:
        __first_name (str): The student's first_name.
        __email (str): The student's last_Name.
        __phone (str): The student's phone number.
    
    """

    def __init__(self, first_name: str, last_Name: str, id: str, phone: str) -> None:
        """
        Args:
            first_name (str): The student's first_name.
            last_Name (str): The student's last_Name.
            phone (str): The student's phone number.
        
        """
        self.__first_name = first_name
        self.__email = last_Name
        self.__id = id
        self.__phone = phone

    def set_student(self, class_first_name: "ClassStudents"):
        """
        Adds the student to a class.

        Args:
            class_first_name (ClassStudents): An instance of the `ClassStudents` class.
        
        """
        class_first_name.add_student(self)

    def get_student(self) -> dict:
        """
        Returns:
            dict: A dictionary containing the student's information.
        
        """
        return [self.__first_name, self.__email, self.__id, self.__phone]

