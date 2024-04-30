# DAY 16
# Python datetime

import datetime
print(dir(datetime))

# Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

print('---------------------------------------------------------------------------------------------------')

# Formating date, time and year with strftime('')
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%A, %d %B %C, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one (MM/DD/YYYY, H:M:S):", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two (DD/MM/YYYY, H:M:S):", time_two)

print('---------------------------------------------------------------------------------------------------')
# String to Time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y") # datetime.strptime(input format, set format)
print("date_object =", date_object)

print('---------------------------------------------------------------------------------------------------')
# Date
from datetime import date
date_today= date.today()
print('The date today: ', date_today)
print('The day today: ', date_today.day)
date_input= date(1993,11,27)
print('The imput date: ', date_input)

print('---------------------------------------------------------------------------------------------------')

# Date
from datetime import time
time_input= time(23,12,30)
print('The date today: ', time_input)
print('The dATE today: ', time_input.hour)

print('---------------------------------------------------------------------------------------------------')

# Difference Between Two Points in Time Using
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("The difference in time t2 and t1:", t3)


print('---------------------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------------------')
# EXERCISE DAY 16
# Get the current day, month, year, hour, minute and timestamp from datetime module
print('EXERCISE DAY 16')
from datetime import datetime
current_date= datetime.now()
current_day = current_date.day
current_year = current_date.year
current_month = current_date.month
current_hour = current_date.hour
current_minute = current_date.minute
current_timestamp = current_date.timestamp()
print('The current date:', current_date)
print('The current date is: {}/{}/{} {}:{}, timestamp: {} '.format(current_year, current_month, current_day, current_hour, current_minute, current_timestamp))

print('---------------------------------------------------------------------------------------------------')

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import date
date_now = date.today()
format_date= date_now.strftime('%M/%d/%Y, %H:%M:%S')
print('Original time: ',date_now)
print('Formated Date: ',format_date)

# Today is 5 December, 2019. Change this time string to time.
today_date = ('5 December, 2019 05:47:09')
format_today_date = datetime.strptime(today_date, '%d %B, %Y %H:%M:%S')
print('String to original date format', format_today_date)
change_format_date = format_today_date.strftime('%A %d %B, %Y  %H:%M:%S')
print('Change date format: ', change_format_date)


# Calculate the time difference between now and new year.
print(datetime.now())
start_hour = int(input('Please input the start hour: '))
start_minute= int(input('Please input the end minute: '))
end_hour = int(input('Please input the shift end hour: '))
end_minute= int(input('Please input the shift end minute: '))

start_time= timedelta( hours=start_hour, minutes=start_minute)
end_time = timedelta(  hours=end_hour, minutes=end_minute)

time_diff = end_time - start_time
print('The total number of shift hours is: ', time_diff)

date_now =datetime.now()
date_1year = datetime(year=2025, month=4, day=30)
diff = date_1year - date_now
print(diff)