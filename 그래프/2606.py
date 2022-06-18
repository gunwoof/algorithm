from sys import stdin as s
from collections import deque as d

computer=int(s.readline())
line_cnt=int(s.readline())

graph=[[] for _ in range(computer+1)]
visited=[0 for _ in range(computer+1)]
que=d()

for _ in range(line_cnt):
    x,y=map(int,s.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for node in graph:
    node.sort()

que.append(1)
visited[1]=1

while que:
    compare_node=que.popleft()

    for node in graph[compare_node]:
        if visited[node] ==0:
            que.append(node)
            visited[node]=1

cnt=0
for i in visited:
    if i==1:
        cnt+=1
print(cnt-1) # "1번 컴퓨터를 통해"이기 때문에 1을 빼줘야함
