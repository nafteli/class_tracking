import pandas as pd
from student import Student


class ReadFile:
    """Class for reading data from an Excel file."""

    def __init__(self, file_path) -> None:
        """Initialize ReadFile object.
        
        Args:
            file_path: str, the path of the Excel file to be read.
        """

        self.file_path = file_path

    def get_data_from(self):
        """Read data from Excel file and return as a list of rows.
        
        Returns:
            A list of rows read from the Excel file.
        """

        df = pd.read_excel(self.file_path)
        return [list(row) for index, row in df.iterrows()]


class SetStudents:
    """Class for creating Student objects from a list of student data."""

    def __init__(self, students_list, classID: int = None) -> None:
        """Initialize SetStudents object.
        
        Args:
            students_list: list, a list of student data in the format of [last name, first name, age, grade].
            classID: int, an optional parameter representing the ID of the class to which the students belong.
        """

        self.students_list = students_list
        self.classID = classID

    def seve_data(self):
        """Create a list of Student objects and save to database."""

        for index in range(len(self.students_list)):
            student = Student(
                self.students_list[index][0][::-1],
                self.students_list[index][1][::-1],
                self.students_list[index][2],
                self.students_list[index][3],
                self.classID,
            )
            #student.save()  # assuming Student class has a method called save() for saving to database
