from sys import stdin as s

N=int(s.readline())
for i in range(N):
    x,y=map(int,s.readline().split())
    print(f"Case #{i+1}: {x} + {y} = {x+y}")