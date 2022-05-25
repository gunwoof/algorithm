from sys import stdin as s

def push(x):
    global stack, top
    stack.append(x)
    top += 1
    Plus_Minus.append("+")

def pop():
    global stack, top
    stack.pop()
    top -= 1
    Plus_Minus.append("-")

n=int(s.readline())

# 1~n까지의 수를 담는 스택
stack=[]
top=-1

# 스택과 비교할 수열
sequence=[int(s.readline()) for i in range(n)]
sequence_top=0

Plus_Minus=[]

i=1
while 1:
    if top == -1 :
        push(i)
        i += 1
    
    
    if stack[top] < sequence[sequence_top]:
        push(i)
        i += 1

    elif stack[top] == sequence[sequence_top]:
        pop()
        sequence_top += 1
        if sequence_top == len(sequence):
            break
    
    # 스택의 peek 비교할 순열의 수 보다 크면 "NO"출력
    elif stack[top] > sequence[sequence_top]:
        print("NO")
        exit()


for i in Plus_Minus:
    print(i)
    

    

