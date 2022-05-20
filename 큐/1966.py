# 찾고 싶은 원소의 인덱스를 계속 체크
# 프린트가 출력 된때마다 카운트 올리기
# 0번째 원소가 max값 보다 작다면 뒤로 넘기기
from sys import stdin as s
from collections import deque as d

T=int(s.readline())

def print_cue():
    global que, answer_cnt, answer_idx
    while 1:
        # 큐의 원소가 하나라면 바로 출력
        if len(que) == 1:
            print(answer_cnt)
            break

        # 0번째 원소가 max값 보다 작다면 뒤로 넘기기
        if que[0] != max(que):
            que.append(que[0]) 
            que.popleft()
            if answer_idx == 0:
                answer_idx = len(que)-1
            else :
                answer_idx -= 1
           
        # 0번째 원소가 max값과 같을때
        else :
            if answer_idx == 0: # 찾고싶은 원소라면 출력
                print(answer_cnt)
                break
            else : # 찾는 원소가 아니라면 삭제
                answer_idx -= 1
            que.popleft()
            answer_cnt +=1
            
        
for i in range(T):
    
    N,M = map(int,s.readline().split())
    que=d(map(int,s.readline().split()))
    answer_idx=M
    answer_cnt=1
    
    print_cue()

    




    
