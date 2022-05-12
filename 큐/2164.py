from sys import stdin as s

def push(x):
    global que,front,rear
    rear+=1
    que.append(x)

def pop():
    global que,front,rear
    front+=1
    
    


N=int(s.readline())
que=[i for i in range(1,N+1)]
front,rear=-1,N-1

while rear-front != 1:
    pop()
    push(que[front+1])
    pop()

print(que[front+1])
    