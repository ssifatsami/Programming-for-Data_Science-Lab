#storing marks
marks = [75, 82, 68, 91, 45]

#calculate total and average marks
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

#find highest and lowest marks
highest = max(marks)
lowest = min(marks)

#count passed courses
passed = 0

for mark in marks:
    if mark >= 50:
        passed = passed + 1

#display the results
print("total Marks:", total)
print("avg Mark:", average)
print("highest Mark:", highest)
print("lowest Mark:", lowest)
print("courses Passed:", passed)




# Store temperatures for Saturday and Sunday
temperatures = (28, 30, 27, 29, 32, 26)

# Display each temperature
for temperature in temperatures:
    print("Temperature:", temperature)

# Find highest and lowest temperatures
highest = max(temperatures)
lowest = min(temperatures)

print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)




# Take input from the user
text = input("Enter a word or short sentence: ")

# Initialize counters
vowels = 0
spaces = 0

# Examine each character
for character in text:
    if character.lower() in "aeiou":
        vowels = vowels + 1

    if character == " ":
        spaces = spaces + 1

# Display the results
print("Number of Characters:", len(text))
print("Number of Vowels:", vowels)
print("Number of Spaces:", spaces)







# Define the function
def calculate_grade(marks):

    # Calculate the average
    average = sum(marks) / len(marks)

    # Determine the grade
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Call the function using five marks
student_marks = [85, 78, 90, 72, 80]

grade = calculate_grade(student_marks)

# Display the result
print("Marks:", student_marks)
print("Average:", sum(student_marks) / len(student_marks))
print("Grade:", grade)





# Store product details in a list of dictionaries
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

# Calculate the total cost
total = 0

for product in products:
    cost = product["price"] * product["quantity"]
    total = total + cost

# Define the discount function
def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total

# Calculate the final price
final_price = apply_discount(total)

# Display the results
print("Total Cost:", total)
print("Final Price After Discount:", final_price)







number = int(input("Enter a number: "))


while number >= 0:
    print(number)
    number = number - 1

print("Countdown finished!")














students = [
    {"name": "Rahim", "department": "CSE",
     "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE",
     "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS",
     "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS",
     "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE",
     "marks": 73, "attendance": 78}
]

passed_students = 0
marks_sum = 0
top_student = students[0]

for s in students:
    print(s["name"], "-", s["marks"])
    marks_sum = marks_sum + s["marks"]
    if s["marks"] >= 50:
        passed_students = passed_students + 1
    if s["marks"] > top_student["marks"]:
        top_student = s

print("Students who passed:", passed_students)
print("Class average:", marks_sum / len(students))
print("Highest mark:", top_student["name"], "with", top_student["marks"])








products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

inventory_value = 0
best_product = None
best_total = 0

for p in products:
    line_total = p["price"] * p["quantity"]
    print(p["name"], "line total:", line_total)
    inventory_value = inventory_value + line_total
    if line_total > best_total:
        best_total = line_total
        best_product = p["name"]

print("Total inventory value:", inventory_value)
print("Highest line total:", best_product, "with", best_total)
