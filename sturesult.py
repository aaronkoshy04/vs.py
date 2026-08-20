# Function to calculate total using recursion
def calculate_total(marks, n):
    if n == 0:
        return 0
    return marks[n - 1] + calculate_total(marks, n - 1)


# Function to calculate average
def calculate_average(total, count):
    return total / count


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to display result
def display_result(name, roll, course, subjects, marks):
    
    # Calculate total using recursion
    total = calculate_total(marks, len(marks))

    # Calculate average
    average = calculate_average(total, len(marks))

    # Calculate grade
    grade = calculate_grade(average)

    # Lambda function for PASS / FAIL
    result = (lambda x: "PASS" if x >= 50 else "FAIL")(average)

    print("\n========================================")
    print("             RESULT")
    print("========================================")

    print("Name       :", name)
    print("Roll No    :", roll)
    print("Course     :", course)

    print("\n----------------------------------------")
    print("Subject              Marks")
    print("----------------------------------------")

    # For loop with range()
    for i in range(len(subjects)):
        print(f"{subjects[i]:<20} {marks[i]}")

    print("----------------------------------------")
    print("Total      :", total)
    print("Average    :", round(average, 2))
    print("Result     :", result)
    print("Grade      :", grade)

    # Grade pattern
    print("\nGrade Pattern:")

    if grade == "A+":
        print("*****")
    elif grade == "A":
        print("****")
    elif grade == "B":
        print("***")
    elif grade == "C":
        print("**")
    elif grade == "D":
        print("*")
    else:
        print("X")


# Main program
while True:

    print("\n========================================")
    print("       STUDENT RESULT ANALYZER")
    print("========================================")

    # Input student details
    name = input("Enter Student Name   : ")
    roll = int(input("Enter Roll Number    : "))
    course = input("Enter Course Name    : ")

    # Subject names
    subjects = ["Python", "HTML", "CSS", "JavaScript", "Django"]

    print("\nEnter marks for 5 subjects\n")

    marks = []

    # For loop and range()
    for subject in subjects:
        mark = float(input(subject + " : "))
        marks.append(mark)

    # Simultaneous assignment
    student_name, student_roll, student_course = name, roll, course

    # Display result
    display_result(
        student_name,
        student_roll,
        student_course,
        subjects,
        marks
    )

    # Ask whether to continue
    choice = input(
        "\nDo you want to enter another student? (yes/no): "
    )

    if choice.lower() == "no":
        print("\nThank you!")
        break
 
   