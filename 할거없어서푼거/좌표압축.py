import sys

n = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))
sorted_points = list(sorted(set(points)))
sorted_dict = {value: index for index, value in enumerate(sorted_points)}

compressed_points = []
for point in points:
    compressed_points.append(sorted_dict[point])

print(*compressed_points)