from datetime import datetime
from dateutil.relativedelta import relativedelta

dob = input('Enter your date of birth (mm-dd-yyyy): ')
date_of_birth = datetime.strptime(dob, '%m-%d-%Y')

diff = relativedelta(datetime.now(), date_of_birth)

current_date = datetime.now()

print(f'Your are {diff.years} years, {diff.months} months, and {diff.days} days old')

print(f'This year is: {current_date.year}')
print(f'Your birth year is: {date_of_birth.year}')
print(f'Your birth month is: {date_of_birth.month}')
print(f'This month is: {current_date.month}')

age = current_date.year - date_of_birth.year
print(f'Your are {age} old')


