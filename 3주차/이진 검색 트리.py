import sys
import bisect
sys.setrecursionlimit(10**5)

preorder = []
postorder = []

for line in sys.stdin:
    preorder.append(int(line.strip()))

def postorder_recursion(preorder):
    root_idx = len(preorder)
    for i in range(1, len(preorder)):
        if preorder[i] > preorder[0]:
            root_idx = i
            break
    left_preorder = preorder[1:root_idx]
    right_preorder = preorder[root_idx:len(preorder)]

    if left_preorder:
        postorder_recursion(left_preorder)
    if right_preorder:
        postorder_recursion(right_preorder)
    postorder.append(preorder[0])

postorder_recursion(preorder)
for node in postorder:
    print(node)