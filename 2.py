name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter course: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")

print("Student details saved successfully.")