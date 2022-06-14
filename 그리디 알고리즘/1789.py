from sys import stdin as s

S=int(s.readline())
cnt=0

for i in range(1,S+1):
    S -= i
    cnt += 1
    if S<0:
        print(cnt-1)
        exit()
    elif S==0:
        print(cnt)
        exit()
    

