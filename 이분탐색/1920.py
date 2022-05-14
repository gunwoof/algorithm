from sys import stdin as s

N=int(s.readline())
A=set(map(int,s.readline().split()))
M=int(s.readline())
MA=list(map(int,s.readline().split()))

for i in MA:
    if i in A:
        print(1)
    else : 
        print(0)
