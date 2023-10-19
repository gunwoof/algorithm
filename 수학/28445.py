from sys import stdin as s
from itertools import product as p

color=[]
for _ in range(2):
    b,t=s.readline().strip().split()
    color.append(b)
    color.append(t)
color=list(set(color))
color.sort()

for i in p(color,repeat=2):
    for j in i:
        print(j,end=" ")
    print()
   
