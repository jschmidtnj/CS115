'''
Created on 11/19/2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 11
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
         as the calling object (self).'''
        new = Date(self.month, self.day, self.year)
        return new
    
    def equals(self, date2):
        '''Decides if self and date2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
        return self.year == date2.year and self.month == date2.month and \
               self.day == date2.day
    
    def tomorrow(self):
        '''this method does not return anything, but instead changes the calling
        object that it represents one calendar day after the date it originally
        represented.
        '''
        days_in_month = DAYS_IN_MONTH[self.month]
        if days_in_month == 28 and (self.year % 4 == 0 and not(self.year % 100 == 0 and self.year % 400 != 0)):
            days_in_month = 29
        if self.day + 1 <= days_in_month:
            self.day += 1
        else: 
            self.day = 1
            self.month +=1
        if self.month > 12:
            self.month = 1
            self.year += 1
    
    def yesterday(self):
        '''like tomorrow, this does not return anything, but instead changes
        the calling object so it is the calendar date 1 before
        '''
        days_in_last_month = DAYS_IN_MONTH[self.month - 1]
        if days_in_last_month == 28 and (self.year % 4 == 0 and not(self.year % 100 == 0 and self.year % 400 != 0)):
            days_in_last_month = 29
        if days_in_last_month == 0:
            days_in_last_month = DAYS_IN_MONTH[12]
        if self.day - 1 > 0:
            self.day -= 1
        else: 
            self.day = days_in_last_month
            self.month -=1
        if self.month == 0:
            self.month = 12
            self.year -= 1
    
    def addNDays(self, N):
        '''this method handles positive integer inputs N, and like tomorrow,
        it does not return anything, but instead changes the calling object
        so that it represents N calendar days after the date it originally
        represented
        '''
        for _ in range(N + 1):
            print(self)
            self.tomorrow()
        self.yesterday()
    
    def subNDays(self, N):
        '''this method handles positive integer inputs N, and like tomorrow,
        it does not return anything, but instead changes the calling object
        so that it represents N calendar days before the date it originally
        represented
        '''
        for _ in range(N + 1):
            print(self)
            self.yesterday()
        self.tomorrow()

    def isBefore(self, date2):
        '''this method should return True if the calling object is a calendar
        date before the input named date2, which is always of object type Date
        If self and date 2 represent the same day, the method should return False
        If self is after date2, the method should return False
        '''
        if (date2).equals(self):
            return False
        if self.year > date2.year:
            return False
        if self.year == date2.year and self.month > date2.month:
            return False
        if self.year == date2.year and self.month == date2.month \
            and self.day > date2.day:
            return False
        return True
    
    def isAfter(self, date2):
        '''this method should return True if the calling object is a calendar
        date after the input named date2, which is always of object type Date
        If self and date 2 represent the same day, the method should return False
        If self is before date2, the method should return False
        '''
        if (date2).equals(self):
            return False
        if self.year < date2.year:
            return False
        if self.year == date2.year and self.month < date2.month:
            return False
        if self.year == date2.year and self.month == date2.month \
            and self.day < date2.day:
            return False
        return True
    
    def diff(self, date2):
        '''this method should return an integer representing the number of days
        between self and date2. self - date2
        '''
        if (date2).equals(self):
            return 0
        numDays = 0
        copy_self = self.copy()
        if copy_self.isBefore(date2):
            while copy_self.isBefore(date2):
                numDays += 1
                copy_self.tomorrow()
            numDays *= -1
        else:
            while copy_self.isAfter(date2):
                numDays += 1
                copy_self.yesterday()
        return numDays
    
    def dow(self):
        '''returns a string to represent the day of the week'''
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                        'Saturday', 'Sunday']
        known_date = Date(11,7,2011)
        #known_day_of_week = 1 # - Monday
        diff_in_days = self.diff(known_date)
        week_day = diff_in_days % 7
        return days_of_week[week_day]

if __name__ == '__main__':
    '''run the program'''
    d = Date(2,28,2011)
    d.tomorrow()
    print('Wednesday is',d)
    d.addNDays(3)
    print(d)
    
    