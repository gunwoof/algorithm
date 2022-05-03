from sys import stdin as s
from math import sqrt

M=int(s.readline())
N=int(s.readline())
prime_list=[]
prime=1


for i in range(M,N+1):
    prime=1
    for j in range(2,int(sqrt(i))+1):
        if i%j == 0:
            prime=0 
    if prime == 1 and i > 1:
        prime_list.append(i)

if len(prime_list) == 0:
    print(-1)
else :
    print(sum(prime_list))
    print(prime_list[0])