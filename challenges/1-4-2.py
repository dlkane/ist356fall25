from datetime import datetime, timedelta

#today = datetime.datetime.now()
#print(today.day)

#birthday = input("Enter your birthday: ")
#test = datetime.strptime(birthday, '%m/%d/%Y')
#test = test + timedelta(days=1)
#print(test)
#print(type(test))
#test_str = test.strftime('%A, %B %d %Y')
#print(test_str)


def parsedate_mdy(text: str) -> datetime:

    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime) -> str:

    return date.strftime('%Y-%m-%d')

text = input('Enter date m/d/y: ')
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)

