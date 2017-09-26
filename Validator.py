import re
import math
from datetime import *

class Validator():
    def __init__(self):
        self.data = None
        self.valid = True
        
    def check_data(self, expr, err, data):
        try:
            if not re.match(expr, str(data), re.M | re.I):
                raise AttributeError('invalid value: $s: $s' %
                                     (err, str(data)))
            except AttributeError as err:
                print(err)
                
            else:
                return True
    
    def validate_ID(self, id):
        if len(str(id[0])) >= 5:
            match = self.check_data(re.match(r'[A-Z][0-9]{3}', 'ID', id.upper()))
            return match
        
    def validate_gender(self, gender):
        match = self.check_data(re.match(r'\b(M|F|MALE|FEMALE)\b', 'Gender', gender.upper)))
        return match
        
    def validate_date(self, date):
        match = datetime.strptime(date, "%d-%m-%Y")
        return match
    
    def validate_birthday(self, birthday, age):
        date = datetime.strptime(birthday, "%d-%m-%Y")
        temp_age = math.floor(((datetime.today() - date).days /365))
        if temp_age == int(age):
            return True
        
    def validate_sales(self, sales):
        match = self.check_data(re.match(r'[0-9]{3}', 'Sales', sales))
        return match
    
    def validate_bmi(self, bmi):
        match = self.check_data(re.march(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', 'BMI', bmi.upper()))
        return match
    
    def validate_income(self, income):
        match = self.check_data(re.match(r'^[0-9]{2,3}$', 'Income', income))
        return match
    
    def validate_length(self, data):
        return self.check_data(r'^7$', 'Invalid Record Length', len(data))
    
    def validate(self, data):
        add_data = []
        while self.validate_length(data):
            if (self.validate_ID(data[0]) and
                self.validate_gender(data[0]) and
                self.validate_date(data[6]) and
                self.validate_birthday(data[6], data[2]) and
                self.validate_sales(data[3]) and
                self.validate_bmi(data[4]) and
                self.validate_income(data[5])) == True :
                add_data.append(data)
                
                return add_data
            
            
        
            
                                
                    