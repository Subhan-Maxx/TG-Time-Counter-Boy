from datetime import datetime
import pytz

def get_data(birth_date, birth_time):
    # Timezone for Asia/Kolkata
    timezone = pytz.timezone("Asia/Kolkata")
    
    # Combine birth date and time
    birth_datetime = datetime.combine(birth_date, birth_time)
    
    # Set the timezone for the birth date
    birth_datetime = timezone.localize(birth_datetime)
    
    # Get the current time in the specified timezone
    current_datetime = datetime.now(timezone)
    
    # Calculate the time difference
    delta = current_datetime - birth_datetime
    
    # Calculate years, months, days, hours, and minutes
    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return years, months, days, hours, minutes
