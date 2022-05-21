from sys import stdin as s

N=int(s.readline())
# 트리의 틀
class node:
    def __init__(self,D,L,R):
        self.data=D 
        self.left=L
        self.right=R

# 전위 순회
def pre_order(node):
    print(node.data, end="")
    if node.left != ".":
        pre_order(tree[node.left])
    if node.right != ".":
        pre_order(tree[node.right])

# 중위 순회
def mid_order(node):
    if node.left != ".":
        mid_order(tree[node.left])
    print(node.data,end="")
    if node.right != ".":
        mid_order(tree[node.right])

# 후위 순회
def post_order(node):
    if node.left != ".":
        post_order(tree[node.left])
    if node.right != ".":
        post_order(tree[node.right])
    print(node.data,end="")


tree={}
# 트리 완성(딕셔너리 사용)
for i in range(N):
    data, left, right=s.readline().split()
    tree[data]=node(data,left,right)

pre_order(tree['A'])
print()
mid_order(tree['A'])
print()
post_order(tree["A"])



        



