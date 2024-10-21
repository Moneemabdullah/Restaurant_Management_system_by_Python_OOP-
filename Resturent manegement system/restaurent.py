from manu import Manu

class Resturent:
    def __init__(self,name):
        self.name = name
        self.employees = [] #detabase
        self.manu = Manu()

    def add_employee(self, employee):
        self.employees.append(employee) 

        
    def view_employee(self):
        print("Employee list")
        for emp in self.employees:
            print(emp.name,emp.email, emp.phone, emp.address)
