from sys import stdin as s

k = int(s.readline())

stack=[]

for i in range(k):
    answer=int(s.readline())
    if answer != 0:
        stack.append(answer)
    else : 
        stack.pop()
print(sum(stack))
