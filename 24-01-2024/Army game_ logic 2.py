import math

def gameWithCells(n, m):
    # Calculate the number of packages needed to cover all bases
    packages_needed = ((n + 1) // 2) * ((m + 1) // 2)

    return packages_needed

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    print(result)
