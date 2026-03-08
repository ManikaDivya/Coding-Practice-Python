student_marks = list(map(int, input("Enter marks: ").split()))

print("------ Student Marks Analysis ------")

print(f"Highest Marks: {max(student_marks)}")
print(f"Lowest Marks: {min(student_marks)}")

total_marks = 0
count = 0

for mark in student_marks:
    total_marks += mark
    count += 1

pass_count = 0
fail_count = 0

print("\nGrades:")

for i in range(len(student_marks)):
    mark = student_marks[i]

    if mark >= 90:
        grade = "A"
        pass_count += 1
    elif mark >= 75:
        grade = "B"
        pass_count += 1
    elif mark >= 60:
        grade = "C"
        pass_count += 1
    elif mark >= 50:
        grade = "D"
        pass_count += 1
    else:
        grade = "Fail"
        fail_count += 1

    print(f"Student {i+1}: {mark} → Grade {grade}")

print(f"\nPass Students: {pass_count}")
print(f"Fail Students: {fail_count}")

print(f"Average Marks: {total_marks / count}")
