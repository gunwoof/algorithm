from sys import stdin as s
from collections import deque as d

N,M,R = map(int,s.readline().split())
graph=[[] for _ in range(N+1)] # 1부터 시작이라 0행은 비움


# 그래프 만들기
for i in range(M):
    x,y=map(int,s.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for node in graph:
    node.sort()

visited=[0]*N # 방문 확인+방문 순서 리스트
visited_cnt=1
que=d() # DFS를 위한 큐

# 시작 노드 큐에 넣고 방문 확인
visited[R-1]=visited_cnt
visited_cnt += 1
que.append(R)


# BFS
while que:
    compare_node=que.popleft()
    
    for node in graph[compare_node]:
        if visited[node-1] == 0:
            que.append(node)
            visited[node-1] = visited_cnt # 큐에 append를 할 때 방문을 확인하자(이래야 시간초과 안 뜸)
            visited_cnt += 1


for i in range(0,N):
    print(visited[i])




