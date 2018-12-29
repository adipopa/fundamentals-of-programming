from domain.student import Student


class StudentValidator:

    def validate(self, student):
        if not isinstance(student, Student):
            raise Exception("Not a student.")

        words_in_name = student.get_name().split()
        if len(words_in_name) < 2:
            raise Exception("The name must include at least 2 words.")
        for word in words_in_name:
            if len(word) < 3:
                raise Exception("Each word in the name must have at least 3 characters.")

        if student.get_attendance_count() < 0:
            raise Exception("The number of attendances must be a positive integer")

        if student.get_grade() < 0 or student.get_grade() > 10:
            raise Exception("The grade must be between 0 and 10.")
