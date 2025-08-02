# Read number of students
n = int(input())

# Initialize dictionary
student_marks = {}

# Read student data
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

# Read query name
query_name = input()

# Calculate average
average = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print result with 2 decimal places
print(f"{average:.2f}")
