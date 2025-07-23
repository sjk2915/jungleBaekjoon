import sys

N = int(sys.stdin.readline().strip())

peoples = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for cur_people in peoples:
    rank = 1
    for compare_people in peoples:
        if (compare_people[0] > cur_people[0]
            and compare_people[1] > cur_people[1]):
            rank += 1

    print(rank)