from sys import stdin as s

N,K=map(int,s.readline().split())
mulcom = 0

if K !=0:
    for i in range(K):
        if mulcom == 0:
            mulcom = N-i
        else :
            mulcom *= N-i
else :
    print(1)
    exit()

answer=mulcom
for i in range(K):
    answer=answer/(i+1)

answer=int(answer)
print(int(answer))

