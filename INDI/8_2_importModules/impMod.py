# from string import Template
# values = {'one': 'Привет', 'copter': 'Квадракоптер'}
#
# t = Template("""
# Ну что, мои хорошие, всем $one
# Это шаблонная строка
# В нее можно вставлять значения по ключам
# Хочу сюда вставлю слово $one, хочу сюда $copter
# """)
#
# print(t.substitute(values))
#

# import sys
# print(sys.getwindowsversion())

# from string import ascii_lowercase,ascii_uppercase, punctuation
# print(ascii_lowercase,ascii_uppercase, punctuation, sep='\n')
# print(ascii_lowercase,ascii_uppercase, punctuation, sep='\n')
# print(ascii_lowercase,ascii_uppercase, punctuation, sep='\n')

import win10toast
from datetime import timedelta,datetime

str_d1 = datetime.now()
str_d2 = '2022/12/30'

# convert string to date object
current_date = datetime.now()
x_date_time = datetime(year=2022, month=12, day=30)
# difference between dates in timedelta
timedelta = x_date_time-current_date

toast = win10toast.ToastNotifier()
toast.show_toast(title= f'VERRY SOON', msg=f'Difference is {timedelta.days} days', duration=3)