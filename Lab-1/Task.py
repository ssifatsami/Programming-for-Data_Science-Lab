num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Quotient: cannot divide by zero")


#Student Profile
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))
print()
print("STUDENT PROFILE")
print("Name       :", name)
print("Student ID :", student_id)
print("Age        :", age)
print("Department :", department)
print("CGPA       :", f"{cgpa:.2f}")


#Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"{celsius} C = {fahrenheit:.2f} F")
print(f"{celsius} C = {kelvin:.2f} K")


#Mark Report for Five Courses
name = input("Enter student name: ")

m1 = float(input("Enter mark for course 1: "))
m2 = float(input("Enter mark for course 2: "))
m3 = float(input("Enter mark for course 3: "))
m4 = float(input("Enter mark for course 4: "))
m5 = float(input("Enter mark for course 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
highest = max(m1, m2, m3, m4, m5)
lowest = min(m1, m2, m3, m4, m5)



# A mark of 50 or higher is a pass
passed = 0
if m1 >= 50:
    passed = passed + 1
if m2 >= 50:
    passed = passed + 1
if m3 >= 50:
    passed = passed + 1
if m4 >= 50:
    passed = passed + 1
if m5 >= 50:
    passed = passed + 1
print()
print("Student Name   :", name)
print("Total          :", total)
print("Average        :", average)
print("Highest mark   :", highest)
print("Lowest mark    :", lowest)
print("Courses passed :", passed)


