class company:
    def com(self):
        name = "PhonePlanet"
        city = "rajkot"
        mono = 1234567898
        print(f"Name : {name}\ncity : {city}\nmobile no : {mono}")

class employee(company):
    def emp(self):
        emp_name = "Nirav"
        desig = "ceo"
        salary = 200000
        print(f"Emp_name : {emp_name}\nDesignation : {desig}\nSalary : {salary}")

e = employee()
e.com()
e.emp()
