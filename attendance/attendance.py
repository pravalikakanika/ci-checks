def mark_attendance(student_id: int) -> str:
    if student_id <= 0:
        raise ValueError("Invalid student ID")
    return f"Attendance marked for student {student_id}"
