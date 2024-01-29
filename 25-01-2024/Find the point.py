def findPoint(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py
    return [rx, ry]

# Read the number of sets of points
num_sets = int(input().strip())

# Process each set of points
for _ in range(num_sets):
    # Read the coordinates of points
    px, py, qx, qy = map(int, input().split())
    
    # Find and print the reflected point
    reflected_point = findPoint(px, py, qx, qy)
    print(*reflected_point)
