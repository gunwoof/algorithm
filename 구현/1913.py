from sys import stdin as s

N = int(s.readline()) # NxN 행렬에서 N
selectN =int(s.readline()) # 좌표를 뽑을 숫자
snList = [[0 for i in range(N)] for j in range(N)] # 달팽이 리스트 0으로 초기화
cnt = 1 # 달팽이 리스트에 들어갈 숫자
rst = (N-1)//2 # 행 시작지점
cst = (N-1)//2 # 렬 시작지점

def snail(number) : # 달팽이 배열의 한 직사각형 만들기
    global N
    global cnt
    global rst
    global cst
    
    # 첫 번째 숫자
    if cnt == 1 :
        snList[(N-1)//2][(N-1)//2] = cnt
        cnt +=1
    
    # 두 번째 숫자 부터
    else :
        for i in range(number-1): # 좌->우(세로 고정)
            snList[cst-1][rst+i] = cnt
            cnt += 1
        rst=rst+(number-2)
        cst=cst-1

        for i in range(1,number): # 상->하(가로 고정)
            snList[cst+i][rst] = cnt
            cnt += 1
        cst=cst+(number-1)

        for i in range(1,number): # 우->좌(세로 고정)
            snList[cst][rst-i] = cnt
            cnt += 1
        rst=rst-(number-1)

        for i in range(1,number): # 하->상(가로 고정)
            snList[cst-i][rst] = cnt
            cnt += 1
        cst=cst-(number-1)

    

# 달팽이 배열 조립
for i in range(1,N+1,2): 
    snail(i)

# selectN의 좌표 찾기
for i in range(N) : 
    for j in range(N) :
        if snList[i][j] == selectN :
            x,y = i,j

# 출력
for i in range(N) :
    print(" ".join(map(str,snList[i])))
print(x+1,y+1)

