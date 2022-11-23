# ref corey schafer

import datetime 
import pytz

# --------- Naive Date time

''' naive datetime'''
d1 = datetime.date(2012, 7, 6) # 2012-07-06
print(d1)   

#d2 = datetime.date(2012, 07, 06) # // leading 0 are not allowed

'''
 week day :- monday = 0 & sunday = 6
 iso week day :- monday = 1 & sunday = 7
'''
tdy = datetime.date.today()  # 2021-10-17
print(tdy.weekday())    # 6
print(tdy.isoweekday()) # 7

'''
time delta => diff between 2 datetime
'''
tdelta = datetime.timedelta(days=7)
print(tdy + tdelta) # date after 1 week

my_bdy = datetime.date(2022, 7, 6)
till_my_bdy = my_bdy - tdy 
print(till_my_bdy.days)    # 262


#------------ datetime

dt = datetime.datetime(2021, 7, 8, 10, 30, 00, 100000)
print(dt.date())  # 2021-07-08


dt_tdy = datetime.datetime.today() # local time zone
dt_now = datetime.datetime.now()   # provide option to pass time zone
dt_utcnow = datetime.datetime.utcnow() # utc time

print(dt_tdy)
print(dt_now)
print(dt_utcnow)

# ------------ timezone

dt = datetime.datetime(2021, 8, 9, 12, 30, 30, tzinfo=pytz.UTC)

# create time zone aware datetime & set it to utc
dt_now = datetime.datetime.now(tz=pytz.UTC) # current time in UTC 
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) # current time in UTC, same as above command

# convert utc timezone into different time zone
# to print time in diff timezone 
dt_pacific = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print(dt_pacific)


# Naive datetime (i.e local datetime) to timezone aware
# local time to Us/Mountain timezone
lcl_dt = datetime.datetime.now()
dt_mtn = pytz.timezone('US/Mountain')

dt_localize = dt_mtn.localize(lcl_dt) # localize local time to US/Mountain timezone
dt_to_mtn_tz = dt_localize.astimezone(pytz.timezone('US/Pacific'))

print(dt_localize)
print(dt_to_mtn_tz)

'''
strftime - convert datetime to string (to format)
strptime - convert string to datetime (given format)
'''

# iso format :
print(dt_to_mtn_tz.isoformat())

# custom format :
print(dt_to_mtn_tz.strftime('%B %d, %Y'))

# Convert datetime str to datetime i.e parse
dt_str = 'July 6, 2021'
dt_p = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_p)


