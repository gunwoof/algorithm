from sys import stdin as s

N=int(s.readline())
tree=[[] for _ in range(N+1)]


for _ in range(N-1):
    x,y=map(int,s.readline().split())
    tree[x].append(y)
    tree[y].append(x)
 
visited=[0 for _ in range(N+1)] # 방문+부모노드 저장
stack=[]

def DFS(tree,stack,visited):
    stack.append(1)
    visited[1]=-1
    
    while stack:
        compare_node = stack.pop()
        
        
        for node in tree[compare_node]:
            if visited[node]==0:
                stack.append(node)
                visited[node] = compare_node

DFS(tree,stack,visited)

for i in visited[2::]:
    print(i)


