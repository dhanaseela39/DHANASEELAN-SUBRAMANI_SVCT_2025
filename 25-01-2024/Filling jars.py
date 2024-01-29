def average_candies(n, operations):
    total_candies = 0

    for operation in operations:
        start_index, end_index, candies = operation
        total_candies += (end_index - start_index + 1) * candies

    average = total_candies // n
    return average

# Read input
n, m = map(int, input().split())

# Read operations
operations = []
for _ in range(m):
    operations.append(list(map(int, input().split())))

# Calculate and print the average
result = average_candies(n, operations)
print(result)
