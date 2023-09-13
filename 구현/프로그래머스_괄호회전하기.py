# 문자열의 길이많큼 돌릴 수 있음
# 올바른지 판단

def solution(s):
    
    s=list(s)
    
    cnt=0
    for i in range(len(s)):
        
        cnt+=check(s)
        
        first=s.pop(0)
        s.append(first)
        
        
    
    answer = cnt
    return answer

def check(s):
    pot=[]
    for i in s:
        pot.append(i)
        if len(pot) > 1:
            if pot[-2] == '[' and pot[-1] == ']':
                pot.pop()
                pot.pop()
                continue # 핵심(append하나에 한짝씩 지워야함)
            if pot[-2] == '(' and pot[-1] == ')':
                pot.pop()
                pot.pop()
                continue
            if pot[-2] == '{' and pot[-1] == '}':
                pot.pop()
                pot.pop()
                continue
    
    if len(pot) == 0:
        return 1
    else:
        return 0