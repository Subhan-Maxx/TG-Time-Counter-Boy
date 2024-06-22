from datetime import datetime

def calculate_age(birth_date, birth_time):
    current_datetime = datetime.now()
    birth_datetime = datetime.combine(birth_date, birth_time)
    
    delta = current_datetime - birth_datetime
    
    # Calculate years
    years = delta.days // 365
    remaining_days = delta.days % 365
    
    # Calculate months
    months = remaining_days // 30
    days = remaining_days % 30
    
    # Calculate hours and minutes
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return years, months, days, hours, minutes
