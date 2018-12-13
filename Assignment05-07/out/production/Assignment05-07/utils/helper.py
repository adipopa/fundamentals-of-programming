from datetime import date


class Helper:
    """
    Helper class for various app related utilities
    """

    @staticmethod
    def resolve_date(date_entry):
        day, month, year = map(int, date_entry.split('/'))
        return date(year, month, day)

    @staticmethod
    def intersection(first_list, second_list):
        return [value for value in first_list if value in second_list]

    @staticmethod
    def average_grade_from_list(grades_list):
        grades_sum = 0
        for grade in grades_list:
            grades_sum += grade.get_grade()
        return grades_sum / len(grades_list) if len(grades_list) != 0 else 0
