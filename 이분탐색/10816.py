from sys import stdin as s
from collections import Counter as c

N= int(s.readline())
Nnumber_li=list(map(int,s.readline().split()))
Nnumber_dic=c(Nnumber_li)

M= int(s.readline())
Mnumber_li=list(map(int,s.readline().split()))

for i in Mnumber_li:
    print(Nnumber_dic[i],end=" ")
