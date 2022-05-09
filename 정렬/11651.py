from sys import stdin as s

N = int(s.readline())
numbers=[]
for i in range(N):
    xy=list(map(int,s.readline().split()))
    numbers.append(xy)


numbers.sort(key=lambda x: (x[1],x[0]))


for i,j in numbers:
    print(i,j)