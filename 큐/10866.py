from sys import stdin as s

def push_frontX(x):
    global dec,end
    end+=1
    dec.insert(0,x)

def push_backX(x):
    global dec,end
    end+=1
    dec.append(x)

def pop_front():
    global dec,end
    if end == -1:
        return -1
    value=dec[0]
    dec.pop(0)
    end -=1
    return value

def pop_back():
    global dec,end
    if end == -1:
        return -1
    value = dec[end]
    dec.pop(end)
    end -=1
    return value

def size():
    global end
    return end+1
    
def empty():
    global end
    if end == -1:
        return 1
    else :
        return 0

def front():
    global dec
    if end == -1:
        return -1
    return dec[0]

def back():
    global dec, end
    if end == -1:
        return -1
    return dec[end]

dec=[]
end=-1

N=int(s.readline())
for i in range(N):
    command=s.readline().rstrip().split()
    if command[0] == 'push_front':
        push_frontX(command[1])
    elif command[0] == 'push_back':
        push_backX(command[1])
    elif command[0] == 'pop_front':
        print(pop_front())
    elif command[0] == 'pop_back':
        print(pop_back())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())