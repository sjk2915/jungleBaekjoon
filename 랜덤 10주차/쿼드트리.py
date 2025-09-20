import sys

N = int(sys.stdin.readline().strip())
image = []
for _ in range(N):
    image.append(list(map(int, sys.stdin.readline().strip())))

def quad_tree(x, y, n):
    is_unified = True
    start_color = image[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if image[i][j] != start_color:
                is_unified = False
                break
        if not is_unified:
            break
    
    if is_unified:
        return start_color
    else:
        half = n // 2
        top_left = quad_tree(x, y, half)
        top_right = quad_tree(x, y + half, half)
        bottom_left = quad_tree(x + half, y, half)
        bottom_rigth = quad_tree(x + half, y + half, half)
        return f'({top_left}{top_right}{bottom_left}{bottom_rigth})'

print(quad_tree(0, 0, N))