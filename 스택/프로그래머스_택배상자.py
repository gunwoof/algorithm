# que와 stack을 이용하여 풀자
# 핵심 : 맞든 틀리든 일단 stack에 넣고 풀자 -> stack에만 집중하자

from collections import deque as d

def solution(order):
    order=d(order)
    number=[i+1 for i in range(len(order))]
    que=d(number)
    stack=[]
    
    cnt=0
    while que:
        stack.append(que.popleft())
        
        while stack and stack[-1] == order[0]:
            cnt+=1
            order.popleft()
            stack.pop()
        
        
            
    
    answer = cnt
    return answer