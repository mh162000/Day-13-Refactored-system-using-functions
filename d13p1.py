def add_student():
student = []

for i in range (3):
    name = input ("Enter name: ")
    marks = int(input("Enter makrs: "))

    student = {
        "name" : name,
        "marks" : marks

    }


    students.append(student)

    return students

def display_students(students):
        for s in students:
    print(s["name"], ":", s["marks'"])


def top_student(students)
top_name = ""
top_marks = 0

for s in students:

    if s["marks"] > top_marks:
        top_marks = s["marks"]
        top_name = s["name"]

        print("Top student:", top_name, "with marks", top_marks)

        students = add_student()
        display_students(students)
        top_student(students)