class Student:
    """
    This class represents a student with the following properties:
    - first_name: str
    - last_name: str
    - id: int
    - phone: str

    Attributes:
        all_students (List[Student]): A list of all student objects created.

    Methods:
        get_all_students(cls) -> List[Student]: Get a list of all the students that exist.

    Properties:
        student: Get and set the student's first name, last name, ID, and phone number.

    """

    all_students = []

    def __init__(
        self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None
    ) -> None:
        """
        Initialize a new student object.

        Args:
            first_name (str): The first name of the student.
            last_Name (str): The last name of the student.
            id (int): The ID of the student.
            phone (str): The phone number of the student.
            classID (int, optional): The ID of the class to which the student belongs. Defaults to None.
        """

        self.first_name = first_name
        self.last_Name = last_Name
        self.id = id
        self.phone = phone
        self.classID = classID
        Student.all_students.append(self)

    @classmethod
    def get_all_students(cls):
        """
        Get a list of all the students that exist.

        Returns:
            List[Student]: A list of all the students that exist.
        """

        return cls.all_students

    @property
    def student(self):
        pass

    @student.getter
    def student(self):
        """
        Get the student's first name, last name, ID, and phone number.

        Returns:
            Tuple[str, str, int, str]: A tuple of the student's first name, last name, ID, and phone number.
        """

        return self.first_name, self.last_Name, self.id, self.phone

    @student.setter
    def student(
        self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None
    ):
        """
        Set the student's first name, last name, ID, phone number, and (optionally) class ID.

        Args:
            first_name (str): The student's new first name.
            last_Name (str): The student's new last name.
            id (int): The student's new ID.
            phone (str): The student's new phone number.
            classID (int, optional): The student's new class ID. Defaults to None.
        """

        self.first_name = first_name
        self.last_Name = last_Name
        self.id = id
        self.phone = phone
        self.classID = classID

    @student.deleter
    def student(self):
        """
        Delete the student's first name, last name, ID, phone number, and class ID.
        """

        del self.first_name, self.last_Name, self.id, self.phone, self.classID

    def __str__(self) -> str:
        """
        Return a string representation of the student object.

        Returns:
            str: A string representation of the student object.
        """

        return f"first name: {self.first_name}\nlast name: {self.last_Name}\nid: {self.id}\nphone: {self.phone}\nclaas id: {self.classID if self.classID else ''}"
