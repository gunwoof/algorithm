# ex 0:[평소문 위치,암호문 위치] 1:[평소문 위치,암호문 위치] ---
from sys import stdin as s

n=int(s.readline())

for i in range(n):
    dic={}
    
    p_c=int(s.readline())
    answer=[0 for _ in range(p_c)]
    ori=list(s.readline().strip().split())
    pas=list(s.readline().strip().split())
    que=list(s.readline().strip().split())

    for i,j in enumerate(ori):
        dic[j]=[i]
    for i,j in enumerate(pas):
        dic[j].append(i)
    
    for i in list(dic.values()):
        answer[i[0]]=que[i[1]]
    
    for i in answer:
        print(i,end=" ")