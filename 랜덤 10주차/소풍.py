import sys

N, K, M = list(map(int, sys.stdin.readline().split()))

dongho_pos = M - 1
current_people = N

exit_order = 0
start_pos = 0

while True:
    removed_idx = (start_pos + K - 1) % current_people
    exit_order += 1
    
    if removed_idx == dongho_pos:
        print(exit_order)
        break
        
    if removed_idx < dongho_pos:
        dongho_pos -= 1
        
    start_pos = removed_idx
    current_people -= 1