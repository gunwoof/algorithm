from sys import stdin as s

def snail(arr):
    global Cst,C,Rst,R,cnt,k,x,y

    # up
    for i in range(Rst,R):
        arr[i][Cst] = cnt
        if k == cnt:
            y,x=i,Cst
        cnt += 1
    Cst += 1
    
    # right
    for i in range(Cst,C) :
        arr[R-1][i] = cnt
        if k == cnt:
            y,x=R-1,i
        cnt += 1
    R -= 1
    
    # down
    for i in range(R-1,Rst-1,-1) :
        arr[i][C-1] = cnt
        if k == cnt:
            y,x=i,C-1
        cnt += 1
    C -= 1

    # left
    for i in range(C-1,Cst-1,-1):
        arr[Rst][i] = cnt
        if k == cnt:
            y,x=Rst,i
        cnt += 1
    Rst += 1
    

C,R = map(int, s.readline().split()) # 끝지점
Cst,Rst = 0,0 # 시작지점
k=int(s.readline()) # 좌표찾을 값
snail_list=[[0 for i in range(C)] for i in range(R)] # 달팽이 배열 0으로 초기화
cnt=1 
x,y=0,0 # k의 좌표

n=min(C,R)/2 # 함수를 돌릴 횟수
if int(n) < n:
    n = int(n)+1
else :
    n =int(n)

for i in range(n): # 달팽이 리스트 완성
    snail(snail_list)
    

if k > cnt :
    print(0)
else :
    print(x+1,y+1)
