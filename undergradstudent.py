'''
Created on Nov 20, 2017

@author: jschm
'''
from student import Student

class UndergradStudent(Student):
    def __init__(self, first_name, last_name, sid, gpa, meal_plan_balance):
        super().__init__(first_name, last_name, sid, gpa) 
        #constructs all of the arguments except for meal plan
        #need to do the superclass first
        self.__meal_plan_balance = meal_plan_balance
    
    @property
    def meal_plan_balance(self):
        return self.__meal_plan_balance
    
    @meal_plan_balance.setter
    def meal_plan_balance(self, meal_plan_balance):
        self.__meal_plan_balance = meal_plan_balance
    
    def __str__(self):
        return super().__str__() + ', meal plan balance: $' \
            + str(self.__meal_plan_balance)

if __name__ == '__main__':
    u1 = UndergradStudent('John', 'Doe', '123456', 1.6, 1000)
    print(u1)
    u1.gpa = 1.2
    print(u1)
    u1.meal_plan_balance = 2000
    print(u1)