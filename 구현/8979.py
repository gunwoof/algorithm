from sys import stdin as s

N,K = map(int,s.readline().split())

country=[]
for i in range(N) :
    country.append(list(map(int,s.readline().split())))
    country[i].append(1)
    

for i in range(N): # 금매달 정렬
    for j in range(i,N):
        if country[i][1]<country[j][1]:
            country[i],country[j] = country[j],country[i]
for i in range(N): # 금매달이 같으면 은매달 정렬
    for j in range(i,N):
        if country[i][2]<country[j][2] and country[i][1]==country[j][1]:
            country[i],country[j] = country[j],country[i]
for i in range(N): # 금매달,은매달이 같으면 동매달 정렬
    for j in range(i,N):
        if country[i][3]<country[j][3] and country[i][1]==country[j][1] and country[i][2]==country[j][2]:
            country[i],country[j] = country[j],country[i]

if N==2: # n=2일때 등수 매기기
    if country[0][1] == country[1][1] and country[0][2] == country[1][2] and country[0][3] == country[1][3]:
        print(1)
    elif country[0][0] == K:
        print(1)
    elif country[1][0] == K:
        print(2)
    exit()
        

for i in range(N-1): # n>2일때 등수 매기기
    if country[i][1] > country[i+1][1]:
        country[i+1][4] = i+1+1
    elif country[i][1] == country[i+1][1] and country[i][2] > country[i+1][2]:
        country[i+1][4] = i+1+1
    elif country[i][1] == country[i+1][1] and country[i][2] == country[i+1][2] and country[i][3] > country[i+1][3]:
        country[i+1][4] = i+1+1
    elif country[i][1] == country[i+1][1] and country[i][2] == country[i+1][2] and country[i][3] == country[i+1][3]:
        country[i+1][4] = country[i][4]

    if country[i][0] == K:
        print(country[i][4])




# 누군가의 깔끔한 코드
n, k = map(int, input().split())
medal = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    medal.append([b, c, d, a])

medal.sort(reverse=True)

for i in range(n):
    if medal[i][3] == k:
        index = i
        
for i in range(n): # 자신보다 잘한 n+1의 등수이므로 K가 속한 배열이 아닌, K가 속한배열과 같은 배열 중 첫번째를 골라서 +1을 한다
    if medal[index][0:3] == medal[i][0:3]:
        print(i + 1)
        break




        