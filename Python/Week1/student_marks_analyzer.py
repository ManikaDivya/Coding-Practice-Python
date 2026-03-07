student_marks = list(map(int, input("Enter marks: ").split()))

print(f"Highest Marks: {max(student_marks)}")
print(f"Lowest Marks: {min(student_marks)}")

total_marks = 0
count = 0

for mark in student_marks:
    total_marks += mark
    count += 1

print(f"Average Marks: {total_marks / count}")
