import sys

X, Y, W, S = list(map(int, sys.stdin.readline().split()))

time = 0
# 직선이동만 이득
if S >= 2*W :
    time = (X + Y) * W
# 직선+대각선이동이 이득
elif 2*W > S > W:
    diag_move = min(X, Y)
    straight_move = abs(X - Y)
    time = diag_move * S + straight_move * W
# 대각선이동만 이득
else:
    if (X + Y) % 2 == 0:
        time = max(X, Y) * S
    else:
        time = (max(X, Y) - 1) * S + W

print(time)