from sys import stdin as s

K,N=map(int,s.readline().split())
rope=[int(s.readline()) for i in range(K)]

start,finish=1,max(rope)

while start <= finish :
    mid=(start+finish)//2
    cnt=0

    for i in rope:
        cnt += i//mid
        
    if cnt >= N:
        start=mid+1
    elif cnt < N:
        finish=mid-1

print(finish)
        
    