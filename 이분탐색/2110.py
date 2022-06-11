from sys import stdin as s

N,C=map(int,s.readline().split())
house=[int(s.readline()) for _ in range(N)]
house.sort()


start,finish = 1,house[-1]-house[0] # 두 좌표 거리의 최소값/최대값

resurt=0

while start<=finish:
    mid=(finish+start)//2 # 비교할 거리
    current = house[0]
    count = 1

    for i in range(1,len(house)): # 두번째 집부터
        if house[i] >= current+mid:
            current=house[i]
            count += 1

    if count >= C:
        start = mid +1
    else:
        finish = mid -1
    
    
print(finish)