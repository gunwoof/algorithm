from sys import stdin as s

def push(braket_element):
    global bracket_stack,bracket_index
    bracket_stack.append(braket_element)
    bracket_index += 1

def pop():
    global bracket_stack,bracket_index
    bracket_stack.pop()
    bracket_index -= 1


T=int(s.readline())
bracket=""

bracket_stack=[]
bracket_index=-1


for i in range(T):
    bracket=s.readline().rstrip()
    mid_print=0 # 중간 탈출 변수
    bracket_stack.clear()
    bracket_index=-1

    for j in range(len(bracket)):
        if bracket[j] ==')' and bracket_index != -1:
            pop()
        elif bracket[j] ==')' and bracket_index == -1:
            print("NO")
            mid_print=1
            break
        else :
            push(bracket[j])
    
    if bracket_index == -1 and mid_print == 0 :
        print("YES")
    elif mid_print == 0:
        print("NO")

    

# 누군가의 깔끔한 코드

for i in range(int(s.readline())):
    VPSstring = s.readline()
    stk = []
    check = False
    for k in VPSstring:
        if k == "(":
            stk.append(k)
        elif k == ")":
            if stk:
                stk.pop()
            else:
                check = True
    
    # 핵심 : NO가 나오는 두가지경우를 한번에 체크
    # 1.여는괄호가 없는 상태에서 닫는괄호가 나올때
    # 2. 여는괄호와 닫는괄호의 개수가 다를 때
    if stk or check: 
        print("NO")
    else:
        print("YES")