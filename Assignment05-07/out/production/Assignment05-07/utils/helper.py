class Helper:

    @staticmethod
    def resolve_date(date):
        day, month, year = map(int, date.split('/'))
        return date(year, month, day)
