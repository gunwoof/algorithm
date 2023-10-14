from sys import stdin as s
from itertools import permutations as p

N=int(s.readline())
number=list(map(int,s.readline().rstrip().split()))
number_sort=sorted(number)

permu=list(p(number_sort,N))

th=0 # 해당 순열의 index
for i in range(len(permu)):
    if permu[i] == tuple(number):
        th=i
        break

for i in range(len(permu)):
    if th-1 ==-1:
        print(-1)
        exit()
    if i == th-1:
        for j in permu[i]:
            print(j,end=" ")
