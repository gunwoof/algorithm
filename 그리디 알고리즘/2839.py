from sys import stdin as s

N = int(s.readline())
cnt=0
min = 10000

if N%5==0 : # 5의 배수라면 먼저 처리
    cnt += N//5
    print(cnt)
elif N%3==0 : # 3의 배수는 다음에 처리
    if N > 15 : # ex) 18같은 경우는 3의 배수이지만 5*3+3*1로 처리할 수 있음
        cnt += (N//15)*3
        N = N - (15*(N//15)) 
    cnt += N//3
    print(cnt)
else : #5의 배수도 아니고 3의 배수도 아닌것을 처리
    i=1
    while N > 5*i:
        cnt += i
        rest = N-(5*i)

        cnt += rest//3
        rest = rest%3

        if rest==0 and min > cnt:
            min = cnt
            
        cnt = 0
        i += 1
    
    if min == 10000: # 5와 3으로 처리하지 못하면 -1처리
        print(-1)
    else :
        print(min)


# 누군가의 깔끔한 코드
a = int(input())

b = 0 # 카운트 변수
while a >= 0 : 
    if a % 5 == 0 : 
        b += (a // 5) 
        print(b)
        break
    a -= 3  
    b += 1 
else :
    print(-1)


