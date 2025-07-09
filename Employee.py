#Employee registration system

class Employee:

    def __init__(self,name,employee_id,department):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        
    def display_info(self):
        print(f'Name:{self.name}')
        print(f'Employee id:{self.employee_id}')
        print(f'Department:{self.department}')



class FullTimeEmployee(Employee):
    
    def annual_salary(self):
        salary=20000
        return salary*12

class PartTimeEmployee(Employee):
   
    def Calculate_payment(self):
        hourly_rate=200
        hours_worked=4
        days_worked=22
        return hourly_rate*hours_worked*days_worked

#........user input......

while True:
    print(".....Employee Registration.....")
    emloyee_type=input("Enter employee type(Full time/Part time):").lower()
    name=input("Enter your name:")
    employee_id=input("Enter Employee id:")
    department=input("Enter department name:")
    
    if emloyee_type=="full time":
        emp=FullTimeEmployee(name,employee_id,department)
        print("....Full Time employee....")
        emp.display_info()
        print(f'Annual salary:{emp.annual_salary()}')
    elif emloyee_type=="part time":
        emp=PartTimeEmployee(name,employee_id,department)
        print("....Part Time employee....")
        emp.display_info()
        print(f'Monthly salary:{emp.Calculate_payment()}')
    else:
        print("Invalid employee type. Please enter full or part time..")
    
    again=input("Do you want to add more employee (yes/no):").lower()
    if again!="yes":
        break
        