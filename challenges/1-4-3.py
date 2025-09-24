from datetime import datetime
from datautils import parsedate_mdy, formatdate_ymd


#text = input('Enter date m/d/y: ')
#date = parsedata_mdy(text)
#date_str = formatdate_ymd(Date)
#print(date_str)

#date = '12/30/2000'
#date_dt_expect = datetime(2000, 12, 30)
#date_dt_actual = parsedate_mdy(date)
#assert date_dt_actual == date_dt_expect

#Main Code
text = input('Enter date m/d/y: ') #12/30/2000
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str) #2000-12-30