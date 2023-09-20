# 스택이었네
def solution(ingredient):
    
    stack=[]
    idx=-1 # 스택 idx(-1부터 시작인것 주의)
    cnt=0 # 햄버거 개수
    
    for i in ingredient:
        stack.append(i)
        idx+=1
        
        if len(stack) > 3:
            if stack[idx] == 1 and stack[idx-1] == 3 and stack[idx-2] == 2 and stack[idx-3] == 1:
                for _ in range(4):
                    stack.pop()
                
                cnt +=1
                idx -=4
    
    answer = cnt
    return answer