from datetime import datetime, date

def filter_only_five_workdays(date_list: date) -> list:
    
    if len(date_list) > 5:
        raise ValueError("Error: the period must not exceed 5 workdays")

    try:
        workdays = []
        for d in date_list:
            if d.isoweekday() < 6: 
                workdays.append(d)     

    except ValueError as e:
        raise ValueError(f"Error: {e}")

    if not workdays:
        raise ValueError("Error: the period must include only workdays")
    
    
    return workdays



        
        
