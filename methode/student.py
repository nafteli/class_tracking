class Student:
    """
    This class represents a student with the following properties:
    - first_name: str
    - last_name: str
    - id: int
    - phone: str
    """

    def __init__(self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None) -> None:
        """
        Initialize a new student object.

        :param first_name: The first name of the student.
        :type first_name: str
        :param last_Name: The last name of the student.
        :type last_Name: str
        :param id: The ID of the student.
        :type id: int
        :param phone: The phone number of the student.
        :type
        """

        self.first_name = first_name
        self.last_Name = last_Name
        self.id = id
        self.phone = phone
        self.classID = classID

    @property
    def student(self):
        pass

    @student.getter
    def student(self):
        """
        Get the student's first name, last name, ID, and phone number.

        :return: A tuple of the student's first name, last name, ID, and phone number.
        :rtype: Tuple[str, str, int, str]
        """
        
        return self.first_name, self.last_Name, self.id, self.phone

    @student.setter
    def student(self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None):
        """
        Set the student's first name, last name, ID, phone number, and (optionally) class ID.

        :param first_name: The student's new first name.
        :type first_name: str
        :param last_Name: The student's new last name.
        :type last_Name: str
        :param id: The student's new ID.
        :type id: int
        :param phone: The student's new phone number.
        :type phone: str
        :param classID: The student's new class ID (optional).
        :type classID: int
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

        :return: A string representation of the student object.
        :rtype: str
        """
        
        return f"first name: {self.first_name}\nlast name: {self.last_Name}\nid: {self.id}\nphone: {self.phone}\nclaas id: {self.classID if self.classID else ''}"
