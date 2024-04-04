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