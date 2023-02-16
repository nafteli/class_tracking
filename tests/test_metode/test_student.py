from methode.student import Student


def test_valedate():
    test = Student('', '', 1234567890, '').student
    assert test == (None, None, None, None)

def test_student_english_name():
    test = Student("ראשון", "סטודנט", 111111118, "052-1234567").student
    assert test == ('ראשון'[::-1], 'סטודנט'[::-1], '111111118', '052-1234567')

def test_student_hebrew_name():
    test = Student('student', 'second', 111111118990, '+97252-1234567').student
    assert test == ('student', 'second', None, '052-1234567')

def test_student_name():
    test = Student('ראשון', 'second', 50012343, '+9722-1234567').student
    assert test == ('ראשון'[::-1], 'second', '050012343', '052-1234567')

def test_student_name():
    test = Student('ראשון/', 'seco,nd', '111111118', '0521234567').student
    assert test == (None, None, '111111118', '052-1234567')

def test_types():
    test = Student(1, True, '', 1).student
    assert test == (None, None, None, None)
