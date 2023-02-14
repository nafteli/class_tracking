class Student:
    """
    This class represents a student with the following properties:
    - first_name: str
    - last_name: str
    - id: int
    - phone: str
    """

    def __init__(self, first_name: str, last_Name: str, id: int, phone: str) -> None:
        """
        Initialize a new student object.

        :param first_name: The first name of the student.
        :param last_Name: The last name of the student.
        :param id: The ID of the student.
        :param phone: The phone number of the student.
        """
        self.first_name = first_name
        self.last_Name = last_Name
        self.id = id
        self.phone = phone
        self.classID = None

    @property
    def student_id(self) -> int:
        """
        Return the ID of the student.
        """
        return self.id

    @student_id.setter
    def student_id(self, id) -> None:
        """
        Set the ID of the student.

        :param id: The new ID..
        """
        self.id = id

    @property
    def student_first_name(self) -> str:
        """
        Return the first name of the student.
        """

        return self.first_name

    @student_first_name.setter
    def student_first_name(self, first_name) -> None:
        """
        Set the first name of the student.

        :param first_name: The new first name.
        """
        self.first_name = first_name

    @property
    def student_last_Name(self) -> str:
        """
        Return the last name of the student.
        """
        return self.last_Name

    @student_last_Name.setter
    def student_last_Name(self, last_name) -> None:
        """
        Set the last name of the student.

        :param last_name: The new last name.
        """
        self.last_Name = last_name

    @property
    def student_phone(self) -> str:
        """
        Return the phone number of the student.
        """
        return self._phone

    @student_phone.setter
    def student_phone(self, phone) -> None:
        """
        Set the phone number of the student.

        :param phone: The new phone number.
        """
        self.phone = phone

    @property
    def class_ID(self) -> int:
        return self.classID

    @class_ID.setter
    def class_ID(self, classID) -> None:
        self.classID = classID

    def __str__(self) -> str:
        """
        Return a string representation of the student object.
        """
        return f"first name: {self.first_name}\nlast name: {self.last_Name}\nid: {self.id}\nphone: {self.phone}\nclaas id: {self.class_ID if self.class_ID else ''}"
