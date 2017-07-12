import datetime

year, month, day = input().split()
date = datetime.date( int( year ), int( month ), int( day ) )
delta = datetime.timedelta( days = float( input()))
date = date + delta
print( date.year, date.month, date.day )
