def connectingTowns(n, routes):
    total_routes = 1
    modulo = 1234567

    for route in routes:
        total_routes = (total_routes * route) % modulo

    return total_routes

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Read the number of towns
    n = int(input().strip())
    
    # Read the number of routes between towns
    routes = list(map(int, input().split()))
    
    # Calculate and print the total number of routes modulo 1234567
    result = connectingTowns(n, routes)
    print(result)
