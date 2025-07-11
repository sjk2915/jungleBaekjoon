import sys

paper = list(map(int, sys.stdin.readline().split()))
paper_w = [paper[0], ]
paper_h = [paper[1], ]
n = int(sys.stdin.readline())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#자르기
for case in cases:
    # 0 가로
    if case[0] == 0:
        new_paper_h = []
        past_value = 0
        is_cut = False
        for item in paper_h:
            if not is_cut:
                if past_value + item < case[1]:
                    new_paper_h.append(item)
                    past_value += item
                elif past_value + item > case[1]:
                    to_cut = case[1] - past_value
                    new_paper_h.append(to_cut)
                    new_paper_h.append(item-to_cut)
                    is_cut = True
            else:
                new_paper_h.append(item)
        paper_h = new_paper_h

    # 1 세로
    elif case[0] == 1:
        new_paper_w = []
        past_value = 0
        is_cut = False
        for item in paper_w:
            if not is_cut:
                if past_value + item < case[1]:
                    new_paper_w.append(item)
                    past_value += item
                elif past_value + item > case[1]:
                    to_cut = case[1] - past_value
                    new_paper_w.append(to_cut)
                    new_paper_w.append(item-to_cut)
                    is_cut = True
            else:
                new_paper_w.append(item)
        paper_w = new_paper_w

papers = [w * h for w in paper_w for h in paper_h]
biggest_paper = max(papers)

print(biggest_paper)