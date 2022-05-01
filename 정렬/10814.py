'''# 시간초과 나오는 코드
from sys import stdin as s

N = int(s.readline())
member=[]
for i in range(N):
    year,name = s.readline().split()
    year= int(year)
    member.append([year,name])

for i in range(N):
    min_index=i
    for j in range(i+1,N):
        if member[min_index][0] > member[j][0]:
            min_index=j

    if min_index != i:
        tmp = member[min_index]
        for k in range(min_index,i,-1):
            member[k] = member[k-1]
        member[i]=tmp


for i,j in member:
    print(i,j)'''



# 내장함수 사용한 코드
from sys import stdin as s

N = int(s.readline())
member=[]
for i in range(N):
    year,name = s.readline().split()
    year= int(year)
    member.append([year,name])

member.sort(key=lambda x:x[0])

for i,j in member:
    print(i,j)
