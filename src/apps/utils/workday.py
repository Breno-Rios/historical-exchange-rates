from datetime import datetime,timedelta, date

class Workdays:

    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end

    def _validation(self):
        if self.start > date.today() or self.end > date.today():
            raise ValueError("Error: the period must not be after today")

        if self.start > self.end:
            raise ValueError("Error: end date must be after start date")
    
        return True

    def filtered_period_is_valid(self, max_days: int)-> bool:
         if self._validation():
            if len(self.generate_workdays()) > max_days:
                return False
            return True
         
    @classmethod
    def filtered_list_is_valid(cls, date_list, max_days: int)-> bool:
        dates= cls.get_workdays(date_list)
        if len(dates) > max_days:
            return False
        return True
    
    def generate_workdays(self)-> list[date]:
        if self._validation():
            workdays = []
            current_date = self.start

            while current_date <= self.end:

                if current_date.isoweekday() < 6:
                    workdays.append(current_date)  

                current_date += timedelta(days=1)

            if not workdays:
                raise ValueError("Error: there are no workdays in the given period")
            
            return workdays
        
    @classmethod
    def get_workdays(cls, date_list) -> list[date]:
        try:
            workdays = []
            for d in date_list:
                if d.isoweekday() < 6: 
                    workdays.append(d)

            if not workdays:
                raise ValueError("Error: there are no workdays in the given period")
            return workdays
        
        except ValueError as e:
            raise ValueError(f"Error: {e}")




        
        
