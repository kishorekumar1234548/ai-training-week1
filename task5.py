import csv
import json

# 1. Writing names into names.txt

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik",]

with open ("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print ("Names written successfully!")

# Reading names with line numbers

with open("names.txt", "r") as file:
    print("\nNames List:)")

    for line_number, name in enumerate(file, start=1):
        print(f"{line_number}. {name.strip()}")


# 2. Creating students.csv
students = [
    {"name": "Arun", "marks": 55},
    {"name": "Priya", "marks": 60},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 45}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "marks"]

    writer = csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("\nstudents.csv created successfully!")

# Reading CSV using DictReader

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\nStudents with marks above 60:")

    for student in reader:
        if int(student["marks"]) > 60:
            print(f"Above 60:  {student['name']} {student['marks']} ")


# 3. Creating students.json

with open("students.json", "w") as file:
     json.dump(students,file, indent=2)

print("\nstudents.jsomn created successfully!")

#  Reading JSON using json.load

with open("students.json", "r") as file:
    data = json.load(file)

    print("\nStudents JSON Data:")

    for student in data:
        print(student["name"],
        student["marks"])


# 4. Handling missing file

try:
    with open("missing.txt", "r") as file:
          
        content = file.read()
        print(content)

except FileNotFoundError:
    print("\nmissing.txt -> File not found")