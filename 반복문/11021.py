from sys import stdin as s

T=int(s.readline())

for i in range(T):
    x,y=map(int,s.readline().split())
    sum=x+y
    print("Case #",end="")
    print(i+1,end="")
    print(":",end=" ")
    print(sum)