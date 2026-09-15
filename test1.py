# Student Marks Analyzer

students = {
    "Aman": [85, 90, 78],
    "Rahul": [72, 65, 80],
    "Priya": [95, 88, 92],
    "Neha": [60, 75, 70]
}

def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks) - 1
    return average


def find_topper(students):
    topper = ""
    highest_marks = 0

    for name, marks in students.items():
        average = calculate_average(marks)

        if average > highest_marks:
            highest_marks = average
            topper = name

    return topper, highest_marks


def generate_report(students):
    print("STUDENT MARKS REPORT")
    print("--------------------")

    for name in students:
        average = calculate_average(students[name])

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        print(f"{name}: Average = {average:.2f}, Grade = {grade}")

    topper, marks = find_topper(students)

    print("\nTopper:", topper)
    print("Topper Average:", marks)


generate_report(students)
