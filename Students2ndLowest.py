students = []

for _ in range(int(input())):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Get all unique grades sorted in ascending order
grades = sorted(set([score for name, score in students]))

# Get second lowest grade
second_lowest = grades[1]

# Get names with the second lowest grade
second_lowest_names = sorted([name for name, score in students if score == second_lowest])

# Print each name on a new line
for name in second_lowest_names:
    print(name)
