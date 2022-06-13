from sys import stdin as s

N,M,R=map(int,s.readline().split())
graph=[[] for _ in range(N+1)]


stack=[]
visited=[0 for _ in range(N+1)]
visited_cnt=1

for i in range(M):
    x,y=map(int,s.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1):
    graph[i].sort() 

stack.append(R)


while stack:
    compare_node=stack.pop()
    if visited[compare_node] ==0:
        visited[compare_node]=visited_cnt
        visited_cnt +=1

    for node in graph[compare_node]:
        if visited[node] == 0:
            stack.append(node)
 
for i in visited[1::]:
    print(i)
