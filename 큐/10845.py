from sys import stdin as s

def push(x):
    global que,front,end
    end += 1
    que.append(x)
    

def pop(): 
    global que,start,end
    if start != end:
        start +=1
        value=que[start]
        return value
    else:
        return -1
    
def size():
    global que,start,end
    return len(que[start+1:end+1])

def empty():
    global que,start,end
    if start==end:
        return 1
    else :
        return 0

def front():
    global que,start,end
    if start==end:
        return -1
    else:
        return que[start+1]

def back():
    global que,start,end
    if start==end:
        return -1
    else:
        return que[end]
    

que=[]
start, end=-1,-1

N=int(s.readline())
for i in range(N):
    command=s.readline().rstrip().split()
    if command[0] == 'push':
        push(command[1])
    if command[0] == 'pop':
        print(pop())
    if command[0] == 'size':
        print(size())
    if command[0] == 'empty':
        print(empty())
    if command[0] == 'front':
        print(front())
    if command[0] == 'back':
        print(back())