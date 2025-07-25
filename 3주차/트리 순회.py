import sys

N = int(sys.stdin.readline().strip())
nodes = {}
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    nodes[node] = (left, right)

def preorder_travel(node):
    if node != '.':
        left, right = nodes[node]
        element.append(node)
        preorder_travel(left)
        preorder_travel(right)

def inorder_travel(node):
    if node != '.':
        left, right = nodes[node]
        inorder_travel(left)
        element.append(node)
        inorder_travel(right)

def postorder_travel(node):
    if node != '.':
        left, right = nodes[node]
        postorder_travel(left)
        postorder_travel(right)
        element.append(node)

element = []
preorder_travel('A')
print(''.join(element))

element = []
inorder_travel('A')
print(''.join(element))

element = []
postorder_travel('A')
print(''.join(element))