from sys import stdin as s

T = int(s.readline())
for i in range(T):
    H,W,N=map(int,s.readline().split())

    # yy 조건
    if N%H == 0:
        yy=str(H)
    else :
        yy=str(N%H)

    # xx 조건
    if N%H == 0:
        xx = (N//H)
    else :
        xx=(N//H)+1

    if xx<10:
        xx="0"+str(xx)
    else:
        xx=str(xx)
        
    print(yy+xx)