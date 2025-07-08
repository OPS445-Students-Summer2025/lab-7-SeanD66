#!/usr/bin/env python3
# Student ID: sdaweng
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second


     #[ insert python code here to check for minute and second 
    #[ attribute here, and carry over when necessary
    #[
    
    #if second reaches 60, carry over 1 to minute
    if sum.second >= 60:
        sum.second = sum.second % 60
        sum.minute += 1
    
    #is minute reaches 60, carry over 1 to hour 
    if sum.minute >= 60:
        sum.minute = sum.minute % 60
        sum.hour += 1
    
    return sum

#time1 = Time(9,50,0)
#9:50:00
#seconds = -1800
#change_time(time1,seconds)

def change_time(time, seconds):
    # if time.second is not less than 0
    time.second += seconds
    if valid_time(time) != True: #checks time.second attribute if it is less than 0
        while time.second >= 60:
            time.second -= 60
            time.minute += 1

        while time.second < 0:
            time.second += 60
            time.minute -= 1

        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1
        
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1
    
    return



def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

if __name__ == "__main__":
    t1 = Time(9,50,0)
    seconds = -1800

    ft = format_time
    change_time(t1, seconds)
    print(format_time(t1))

    