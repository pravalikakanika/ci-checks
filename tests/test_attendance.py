from attendance.attendance import mark_attendance


def test_mark_attendance_valid():
    assert mark_attendance(1) == "Attendance marked for student 1"


def test_mark_attendance_invalid():
    try:
        mark_attendance(0)
        assert False, "Expected ValueError"
    except ValueError:
        pass
