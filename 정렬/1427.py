from sys import stdin as s

N=list(map(int,s.readline().rstrip()))
N.sort(reverse=True)

for i in N:
    print(i,end="")