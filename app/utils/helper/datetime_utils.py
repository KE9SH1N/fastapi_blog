from datetime import datetime

def format_datetime(dt: datetime):
    if not dt:
        return None

    return dt.strftime("%Y-%m-%d, %I:%M %p")