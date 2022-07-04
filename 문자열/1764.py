from sys import stdin as s
from collections import Counter as c

# Counter을 이용한 풀이
'''N,M=map(int,s.readline().split())

listen_answer=[s.readline().rstrip() for _ in range(N+M)]

listen_answer=c(listen_answer)
overlap=[]

for i,j in listen_answer.items():
    if j > 1:
        overlap.append(i)
overlap.sort()
print(len(overlap))
for i in overlap:
    print(i)'''

# 집합을 이용한 풀이
N,M=map(int,s.readline().split())

listen=set(s.readline().rstrip() for _ in range(N))
answer=set(s.readline().rstrip() for _ in range(M))
overlap=list(listen&answer)
overlap.sort()
print(len(overlap))
for i in overlap:
    print(i)


        

