nowh, nowm = input().split()
time= input()

H = int(nowh)
M = int(nowm)
T = int(time)


if M+T < 60 :
    M = M+T
elif M+T>=60 :
    M = M+T-60
    H = H+1
    if H == 24 :
        H = 0
    while M >= 60 :
        M = M-60
        H = H+1
        if H == 24 :
            H = 0
print(H,M)


# 누군가의 깔끔한 코드
'''h,m=map(int,input().split())
t=int(input())

h += t // 60 #나누고 정수부분만
m += t % 60 #나누고 나머지 
if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24
    
print(h, m)'''




