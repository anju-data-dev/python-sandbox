# 1. Calculating age

import datetime

now = datetime.datetime.now()
year_of_birth = input('Which year were you born? ')
age = now.year - int(year_of_birth)
print(f'You are {age} years old.')