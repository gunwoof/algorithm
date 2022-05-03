from sys import stdin as s
from math import sqrt 

number = int(s.readline())
numbers=list(map(int,s.readline().split()))
cnt=0

for i in numbers:
    prime=1
    for j in range(2,int(sqrt(i))+1):
        if i%j ==0:
            prime=0
    if prime==1 and i != 1:
        cnt+=1

print(cnt)