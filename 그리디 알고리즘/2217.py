from sys import stdin as s

N=int(s.readline())
lope=[0 for i in range(N)]
max_weight=0

for i in range(N):
    lope[i]=int(s.readline())
lope.sort()

for i in range(len(lope)):
    if max_weight < lope[i]*(len(lope)-i):
        max_weight=lope[i]*(len(lope)-i)
print(max_weight)
