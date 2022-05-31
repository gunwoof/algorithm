from sys import stdin as s
from collections import deque as d

def left_que(): # 좌 로테이트
    global que
    que.append(que[0])
    que.popleft()

def right_que(): # 우 로테이트
    global que
    que.rotate(1)

N,M=map(int,s.readline().split())
compare=list(map(int,s.readline().split()))

que=[i+1 for i in range(N)]
que=d(que)
cnt = 0

i=0
while 1:
    if que[0] != compare[i]:
        if len(que) - que.index(compare[i]) > que.index(compare[i]): # 좌로 로테이트 할지 vs 우로 로테이트 할지          
            left_que()
            cnt += 1
        else :
            right_que()
            cnt += 1
    else :
        que.popleft()
        i += 1

    if i == len(compare):
        print(cnt)
        exit()


