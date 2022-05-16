from sys import stdin as s
from collections import deque as d

def R():
    global n_list
    n_list.reverse()

# 좌 삭제
def l_D(): 
    global n_list
    n_list.popleft()

# 우 삭제
def r_D():
    global n_list
    n_list.pop()

T = int(s.readline()) # 테스트의 횟수

for i in range(T):
    error = 0
    p = list(s.readline().rstrip()) # 명령

    n = int(s.readline()) #배열의 개수
    # 배열 정리 
    n_list=d(s.readline()[1:-2].split(",")) 
    if n_list[0]=="":
        n_list.clear()


    # 시간 줄이기 핵심 : 뒤집기를 제일 마지막에 함!!
    j=0
    R_cnt=0
    while j < len(p):
        # "D"가 나오기 전까지의 뒤집기의 횟추 카운트
        while p[j] == "R":
            R_cnt += 1
            if j != len(p)-1:
                j += 1
            else : # index초과를 막아줌
                break
            
        # "D"가 나오기 전까지의 뒤집기의 횟수로 왼쪽에서 삭제할지 오른쪽에서 삭제할지 정함(시간줄이기의 핵심)
        if p[j] == "D" and len(n_list) > 0 :
            if R_cnt%2 !=0:
                r_D()
            elif R_cnt%2 ==0 :
                l_D()
        elif p[j] == "D"and len(n_list) == 0:
            print("error")
            error=1
            break
        j += 1

    # 뒤집기의 개수를 한번에 모아서 마지막에 함(시간줄이기의 핵심)
    if R_cnt%2 !=0 and R_cnt%2 > 0:
        R()
   
    # 출력    
    if error == 0:
        print("["+",".join(n_list)+"]")



        
        
        
        
        




