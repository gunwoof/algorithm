from sys import stdin as s

stack=[]
cnt=-1

def push(x):
    global stack, cnt
    stack.append(x)
    cnt +=1

def pop():
    global stack, cnt
    if cnt == -1 : # 스택이 비어있을 때
        return -1

    pop_print=stack[cnt]
    stack.pop()
    cnt -=1
    return  pop_print

def size():
    global cnt
    return cnt+1

def empty():
    global cnt
    if cnt == -1:
        return 1
    else :
        return 0

def top():
    global stack, cnt
    if cnt == -1 : # 스택이 비어있을 때
        return -1
    return stack[cnt]

N=int(s.readline())
for i in range(N):
    order=s.readline().rstrip().split()
    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        print(pop())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "top":
        print(top())