# 자료구조를 계속 새로만드니까 시간초과 -> 자료구조를 수정하는 방식
from collections import Counter as c

def solution(topping):
    cnt=0
    bro1=c(topping)
    bro2=set()
    for i in topping:
        bro1[i] -=1
        if bro1[i] ==0:
            bro1.pop(i)
        
        bro2.add(i)
        
        if len(bro1.keys())==len(bro2):
            cnt+=1
    
    answer = cnt
    return answer