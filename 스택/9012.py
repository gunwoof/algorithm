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

    



    
