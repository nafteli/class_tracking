import re


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

        self.first_name = self.__Validate_name(first_name)
        self.last_Name = self.__Validate_name(last_Name)
        self.id = self.__validate_ID(id)
        self.phone = self.__validate_phone(phone)
        self.classID = self.__validate_classID(classID)
        Student.all_students.append(self)

    def __Validate_name(self, name) -> str:
        """
        Validates the input name string to ensure that it only contains Hebrew or English characters and spaces.
        If the input name is valid, the function returns the name string in reverse order.
        If the input name is invalid, a ValueError is raised with an error message.

        Args:
            name (str): A string representing the name to be validated.

        Returns:
            str: The input name string in reverse order if the name is valid, otherwise None.

        Raises:
            ValueError: If the input name is not a string or if it contains characters other than Hebrew or English and spaces.

        """

        try:
            if not isinstance(name, str) or not re.match(r"^[א-ת\s]+$|^[a-zA-Z\s]+$", name):
                raise ValueError(f"{name} Is Invalid Hebrew or English name")
            return name[::-1] if re.match("^[א-ת\s]+$", name) else name
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def __validate_phone(self, phone) -> str:
        """
        Validates the input phone string to ensure that it is a valid Israeli phone number and formats it with hyphens.
        If the input phone number is valid, the function returns the formatted phone number.
        If the input phone number is invalid, a ValueError is raised with an error message.

        Args:
            phone (str): A string representing the phone number to be validated and formatted.

        Returns:
            str: The formatted phone number string if the phone number is valid, otherwise None.

        Raises:
            ValueError: If the input phone number is not a string or if it is not a valid Israeli phone number.

        """

        israeli_phone_regex = r"^(?:\+972|0)(?:-)?(?:5[02-9]|[2-489]\d)(?:(?<=\d)-|\s*)\d{3}(?:(?<=\d)-|\s*)\d{4}$"
        try:
            if not isinstance(phone, str) or not re.match(israeli_phone_regex, phone):
                raise ValueError(f"{phone} Is Invalid Israeli phone number")

            # Remove any whitespace characters from the phone number
            stripped_phone_number = re.sub(r"\s", "", phone)

            # Replace the cuntry code to 0
            formatted_phone_number = re.sub(r"^\+972-?|0-?", "0", stripped_phone_number)

            # Use re.sub() to format the phone number with hyphens
            formatted_phone_number = re.sub(
                r"^(\d{3})(\d{3})(\d{4})$", r"\1-\2\3", formatted_phone_number
            )
            return formatted_phone_number
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def __validate_classID(self, classID) -> int:
        """
        Validates the input classID integer to ensure that it is a valid class ID.
        If the input classID is valid, the function returns it. Otherwise, it returns None.

        Args:
            classID (int): An integer representing the class ID to be validated.

        Returns:
            int: The input class ID integer if it is valid, otherwise None.

        """

        classIDs = [2]
        return classID if classID in classIDs else None

    def __validate_ID(self, id) -> str:
        """
        Validates the input ID string to ensure that it is a valid Israeli ID number.
        If the input ID number is valid, the function returns it with leading zeros.
        If the input ID number is invalid, None is returned.

        Args:
            id (str or int): A string or integer representing the ID number to be validated.

        Returns:
            str: The validated ID number string with leading zeros if it is valid, otherwise None.

        """
        try:
            # Convert the input to a string and remove any spaces
            id = str(id).strip()
            # If the input is not a number or if it is too long, return None
            if len(id) > 9 or not id.isnumeric():
                return None
            # Add zeros to the start of the ID number until it has 9 digits
            id = id.rjust(9, "0")
            # Check if the ID number is valid using some math:
            # - Multiply each digit by 1 or 2, depending on its position (odd or even)
            # - Add up the digits of the results
            # - If the sum is divisible by 10, the ID is valid
            if (
                sum(
                    (digit - 9) if digit > 9 else digit
                    for digit in [
                        int(digit) * ((i % 2) + 1) for i, digit in enumerate(id)
                    ]
                )
                % 10
                != 0
            ):
                return None
            # If the ID number is valid, return it with leading zeros
            return id

        except ValueError as e:
            # If something goes wrong during the validation, catch the error and return None
            print(f"Error: {e}")
            return None

    @classmethod
    def get_all_students(cls) -> list:
        """
        Get a list of all the students that exist.

        Returns:
            List[Student]: A list of all the students that exist.
        """

        return cls.all_students

    @property
    def student(self) -> None:
        pass

    @student.getter
    def student(self) -> tuple:
        """
        Get the student's first name, last name, ID, and phone number.

        Returns:
            Tuple[str, str, int, str]: A tuple of the student's first name, last name, ID, and phone number.
        """

        return self.first_name, self.last_Name, self.id, self.phone

    @student.setter
    def student(
        self, first_name: str, last_Name: str, id: int, phone: str, classID: int = None
    ) -> None:
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
    def student(self) -> None:
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
