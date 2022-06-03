from sys import stdin as s

N,M,R = list(map(int,s.readline().split()))

visited=[False]*(N) # 방문 여부
stack=[] 

order={} # 숫자 순서대로 출력
cnt=1

# 그래프 완성
graph={}
for i in range(M):
    x,y=map(int,s.readline().split())
    if x not in graph:
        graph[x] = [y]
    else :
        graph[x].append(y)

    if y not in graph:
        graph[y] = [x]
    else : 
        graph[y].append(x)

# 오름차순으로 하기위한 하위노드 정렬
for i in graph.keys():
   graph[i].sort(reverse=True)
    

# DFS
stack.append(R)
while stack:
    compare_node=stack.pop()
    visited[compare_node-1]=True

    if compare_node not in order.keys():
        order[compare_node]=cnt
        cnt += 1
    
    for i in graph[compare_node]:
        if visited[i-1] == False:
            stack.append(i)

            
# 숫자 순서대로 출력
for i in range(1,N+1):
    if i in order.keys():
        print(order[i])
    else:
        print(0)
   







# 재귀는 에러뜸(백준에서 에러)
'''def dfs(R,graph,visited,order):
    global cnt

    visited[R-1]=True
    order[R]=cnt
    cnt += 1
    
    for i in sorted(graph[R]):
        if visited[i-1] == False:
            dfs(i,graph,visited,order)'''