from myclasses import *

hr1 = HREmployee('Jeniffer', 'Connely', 200)
en1 = EnggEmployee('Tom', 'Cruise', 30)

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