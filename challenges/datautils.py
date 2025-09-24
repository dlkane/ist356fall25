from datetime import datetime, timedelta

def parsedate_mdy(text: str) -> datetime:

    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime) -> str:

    return date.strftime('%Y-%m-%d')