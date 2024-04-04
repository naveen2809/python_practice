class Employee:

    def __init__(self, firstName, lastName, empNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.empNumber = empNumber
        self.email = str(firstName)+"."+str(lastName)+"@mycompany.com"

    def get_fullname(self):
        return str(self.firstName + " " + self.lastName)

    def get_email(self):
        return self.email.lower()

    def get_empnumber(self):
        return self.empNumber

class HREmployee(Employee):

    department = 'HR'

    def __init__(self, firstName, lastName, empNumber):
        super().__init__(firstName, lastName, empNumber)

    def get_department(self):
        return self.department

class EnggEmployee(Employee):

    department = 'Engineering'

    def __init__(self, firstName, lastName, empNumber):
        super().__init__(firstName, lastName, empNumber)

    def get_department(self):
        return self.department

hr1 = HREmployee('Mike', 'Lewis', 100)
en1 = EnggEmployee('John', 'Millman', 200)

print("HR Employee Details")
print("Full Name: ", hr1.get_fullname())
print("Employee Number: ", hr1.get_empnumber())
print("Email: ", hr1.get_email())
print("Department: ", hr1.get_department())

print("\nEngineering Employee Details")
print("Full Name: ", en1.get_fullname())
print("Employee Number: ", en1.get_empnumber())
print("Email: ", en1.get_email())
print("Department: ", en1.get_department())