def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_best_divisor(n):
    best_divisor = 1
    max_digit_sum = 0

    for divisor in range(1, n + 1):
        if n % divisor == 0:
            digit_sum = sum_of_digits(divisor)

            if digit_sum > max_digit_sum or (digit_sum == max_digit_sum and divisor < best_divisor):
                max_digit_sum = digit_sum
                best_divisor = divisor

    return best_divisor

# Read input
n = int(input().strip())

# Find and print the best divisor
result = find_best_divisor(n)
print(result)
