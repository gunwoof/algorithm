from sys import stdin as s

def push(x):
    global stack, top
    stack.append(x)
    top += 1

def pop():
    global stack, top
    stack.pop()
    top -= 1

K=int(s.readline())
stack=[]
top = -1

for i in range(K):
    number=int(s.readline())
    if number != 0:
        push(number)
    else:
        pop()

print(sum(stack))
