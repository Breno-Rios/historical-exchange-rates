from datetime import date

class DateFormatter(date):

    @classmethod
    def fromisoformat(cls, date_string: str):
        try:
            return super().fromisoformat(date_string)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}, must be 'YYYY-mm-dd'")
