def add_students():
    students = []
    
    for i in range(3):
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        
        student = {
            "name": name,
            "marks": marks
        }
        
        students.append(student)
    
    return students


def display_students(students):
    for s in students:
        print(s["name"], ":", s["marks"])


def find_top_student(students):
    top_name = ""
    top_marks = 0

    for s in students:
        if s["marks"] > top_marks:
            top_marks = s["marks"]
            top_name = s["name"]

    print("Top student:", top_name)
    print("Marks:", top_marks)


# main program
students = add_students()
display_students(students)
find_top_student(students)