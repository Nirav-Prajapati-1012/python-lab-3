class Employee:
    def __init__(self,emp_name,date_of_join,desig,salary):
        self.emp_name = emp_name
        self.date_of_join = date_of_join
        self.desig = desig
        self.salary = salary

dis = Employee("Nirav","10-12-2022","CEO",200000)
print(f"Employee name : {dis.emp_name}\nDate of Join : {dis.date_of_join}\nDesignation : {dis.desig}\nSalary : {dis.salary}")
