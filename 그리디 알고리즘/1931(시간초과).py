from sys import stdin as s

number = int(s.readline())
sh = []
council = []

# nX2 행렬로 값 넣음
for i in range(number) :
    n,m = map(int,s.readline().strip().split())
    sh.append([n,m])

# 끝 시간의 오름차순 정렬
sh.sort(key=lambda x:x[1])

# 최대 회의의 개수
councnt = 0
for i in range(number) : # 기준
    a = sh[i][1]
    council.append([sh[i][0],sh[i][1]]) # 기준값은 먼저넣음
    for j in range(i+1,number) : # 회의 시작시간이 이전회의 끝 시간보다 크면 넣음
        if a < sh[j][0]:
            council.append([sh[j][0],sh[j][1]]) 
            a = sh[j][1]
    

    if councnt < len(council): # 회의의 최대 개수
        councnt = len(council)
    
    council.clear()

print(councnt)