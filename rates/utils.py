from datetime import datetime,timedelta,date

def generate_date_range(start_date, end_date):
    fmt = "%Y-%m-%d"
    try:
        # change as strings to obj date
        start = datetime.strptime(start_date, fmt).date()
        end    = datetime.strptime(end_date,    fmt).date()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")
    
    if start > date.today():
        raise ValueError("The 'start_date' cannot be after today")
    if start > end:
        raise ValueError("The 'end_date' cannot be earlier than the 'start_date'")
    if end - start > timedelta(days=5):
        raise ValueError("The period between 'start_date' and 'end_date' cannot exceed 5 days")
    
    date_list = []
    current_date = start

    while current_date <= end:
        date_list.append(current_date.isoformat())  # 'YYYY-MM-DD'
        current_date += timedelta(days=1)

    return date_list
            
    