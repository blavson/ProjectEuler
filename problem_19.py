weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
def isLeapYear(year):
   if ((year % 4 == 0) and (year % 100 !=0)) or( year % 400 == 0):
      return True
   else:
      return False         


def getSundays():
   normal_num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   leap_num_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

   days = 0
   for year in range(1900, 2001):
      days_in_year = 0
      for m in range(0,12):
         if (m ==1) and ( (year % 4 == 0) and (year % 100 !=0)) or( year % 400 == 0):
            days += leap_num_of_days[m]
            days_in_year += leap_num_of_days[m]
         else:
           days += normal_num_of_days[m]
           days_in_year += normal_num_of_days[m]
      print(days_in_year)
   print(days)           
   
def getWeekdayFromFirst(either_365_or_366):
   return 7 -(either_365_or_366 % 7) 
   
print(getWeekdayFromFirst(366))      
#getSundays()
