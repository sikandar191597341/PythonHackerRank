# Read input
n = int(input())
arr = list(map(int, input().split()))

# Find the highest score
max_score = max(arr)

# Remove all occurrences of the highest score
while max_score in arr:
    arr.remove(max_score)

# Now find the new max, which is the runner-up
runner_up = max(arr)
print(runner_up)
