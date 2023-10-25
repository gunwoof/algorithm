from sys import stdin as s
from collections import deque as d

def dfs(graph,N,V):
    visited=[0]*(N+1) # 노드 1번부터 시작
    answer=[] # 출력 리스트
    

    stack=[]
    stack.append(V)
    answer=[V]
    visited[V]=1
    

    while stack:
        front_noed=stack.pop()
        if visited[front_noed] == 0:
            visited[front_noed] = 1
            answer.append(front_noed)

        for i in graph[front_noed]:
            if visited[i] == 0:
                stack.append(i)

    return answer
    
def bfs(graph,N,V):
    visited=[0]*(N+1) # 노드 1번부터 시작
    answer=[] # 출력 리스트
    

    que=d()
    que.append(V)
    answer=[V]
    visited[V]=1

    while que:
        front_noed=que.popleft()
        if visited[front_noed] == 0:
            
            visited[front_noed] = 1
            answer.append(front_noed)

        for i in graph[front_noed]:
            if visited[i] == 0:
                que.append(i)

    return answer




N,M,V=map(int,s.readline().split())

graph=[[] for _ in range(N+1)] # 노드 1번부터 시작

for _ in range(M):
    x,y=map(int,s.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 내림차순으로 정렬해야 dfs에서는 작을 수 부터 탐색할 수 있음
for node in graph:
    node.sort(reverse=True)
dfs_visited=dfs(graph,N,V)

# 오름차순으로 정렬해야 bfs에서는 작을 수 부터 탐색할 수 있음
for node in graph:
    node.sort()
bfs_visited=bfs(graph,N,V)


for i in range(len(dfs_visited)):
    print(dfs_visited[i],end=" ")
print()
for i in range(len(dfs_visited)):
    print(bfs_visited[i],end=" ")










