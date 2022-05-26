from sys import stdin as s

N,M=map(int,s.readline().split())
trees=list(map(int,s.readline().split()))

start=0
finish=max(trees)

while start <= finish:
    mid=(start+finish)//2
    cnt=0 # 나무의 개수
    
    for i in trees:
        if cnt > M:
            break

        if i >= mid:
            cnt += i-mid
        
    
    
    if cnt >= M:
        start=mid+1
    else :
        finish=mid-1

print(finish)
    
    
