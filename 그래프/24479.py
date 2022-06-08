from sys import stdin as s

N,M,R = list(map(int,s.readline().split()))

visited=[0 for _ in range(N+1)] # 0번 노드가 없기 때문에 비움
visited_cnt=1

stack=[]

graph=[[] for _ in range(N+1)] # 0번 노드가 없기 때문에 비움
for _ in range(M):
    x,y=map(int,s.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for node in graph:
    node.sort(reverse=True)

stack.append(R)
visited[R]=visited_cnt
visited_cnt += 1

while stack:
    compare_node=stack.pop()
    if visited[compare_node] == 0:
        visited[compare_node] = visited_cnt
        visited_cnt += 1

    for node in graph[compare_node]:
        if visited[node] == 0:
            stack.append(node)
         
            

for i in range(1,N+1):
    print(visited[i])






