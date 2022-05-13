from sys import stdin as s

# 큐 삭제 연산
def pop():
    global cir_que,front
    value=cir_que[front]
    cir_que[front]=0
    return value

N,K=map(int,s.readline().split())
cir_que=[i for i in range(1,N+1)] # 원형큐
front=-1

Josephus_permutation=[] # 요세푸스 순열을 담는 그릇


while len(Josephus_permutation) != N:
    j=0
    while 1:
        # 원형큐
        if front == N-1:
            front = front-N

        # pop으로 삭제된 연산 건너뛰기
        if cir_que[front+1] !=0:
            front +=1
            j+=1
        else:
            front +=1

        if j==K :
            break
            
    Josephus_permutation.append(pop())

print("<",end="")
for i in range(len(Josephus_permutation)):
    print(Josephus_permutation[i],end="")
    if i != len(Josephus_permutation)-1:
        print(", ",end="")
print(">")

    
