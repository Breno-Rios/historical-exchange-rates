
from datetime import datetime,timedelta

class DateGenerator():
    
    @staticmethod
    def range_dates(start: datetime , end: datetime):

        if start > end:
            raise ValueError("Error: end date must be after start date")

        if not isinstance(start, datetime) and isinstance(end, datetime):
            raise ValueError('error: the types of dates must be a datetime')

        date_list = []
        current_date = start

        while current_date <= end:
            date_list.append(current_date)  
            current_date += timedelta(days=1)
        return date_list

    
    @staticmethod
    def range_iso_dates(start: datetime, end: datetime):
        return [d.isoformat() for d in DateGenerator.range_dates(start, end)]
    