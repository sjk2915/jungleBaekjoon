import sys  

n = (int)(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check_color(n, r, c):
    color = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != color:
                return False
    return True

white_count = 0
blue_count = 0
def paper_conting(n, r, c):
    global white_count
    global blue_count
    if check_color(n, r, c):
        if paper[r][c] == 0:
            white_count += 1
        else:
            blue_count += 1
        return 
    
    else:
        half = n // 2
        # 1. 왼쪽 위 사분면
        paper_conting(half, r, c)    
        # 2. 오른쪽 위 사분면
        paper_conting(half, r, c + half)
        # 3. 왼쪽 아래 사분면
        paper_conting(half, r + half, c)
        # 4. 오른쪽 아래 사분면
        paper_conting(half, r + half, c + half)

paper_conting(n, 0, 0)
print(white_count)
print(blue_count)