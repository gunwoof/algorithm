from sys import stdin as s

T=int(s.readline())
apart=[[0 for i in range(15)] for i in range(15)] # 1 ≤ 층,호 ≤ 14의 제한을 주었기 때문

for i in range(15):
    for j in range(15):
        if i==0 :  
            apart[i][j]=j+1
        elif j==0:
            apart[i][j]=1
        else :
            apart[i][j]=apart[i][j-1]+apart[i-1][j]

for i in range(T):
    k=int(s.readline()) # k층(0층부터 시작)
    n=int(s.readline()) # n호(1호부터 시작)
    print(apart[k][n-1])

