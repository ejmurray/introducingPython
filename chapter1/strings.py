__author__ = 'Ernest'
# Material from chapter 2 of Introduction to python
# to save a session from the console in ipython use the following
# command - %save my_session 1-20
# where %save is teh save command, my_session is the file name
# and 1-20 are the lines that you want to save.
# this data has been added to github as a new repo
# and this line

letters = 'abcdefghijklmnopqrstuvwxyz'

letters[-1]

letters[-2]

letters[25]

letters[10]

# 2.2
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print('There are', seconds_per_hour, 'seconds in an hour.')

# 2.3
hours_per_day = 24
seconds_per_day = hours_per_day * seconds_per_hour
print('There are', seconds_per_day, 'seconds in a day.')

# 2.5 float division
hours_per_day = seconds_per_day / seconds_per_hour
print('There are', hours_per_day, 'hours per day.')

# 2.6 integer division
hours_per_day = seconds_per_day // seconds_per_hour
print('There are', hours_per_day, 'hours per day.')
