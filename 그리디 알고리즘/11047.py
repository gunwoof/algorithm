n, answerMoney = map(int,input().split())
money=[]
cnt = 0
standcnt = 0
stand =0

for i in range(n) :
    money.append(int(input()))
money.sort(reverse = True)

for i in range(n):  # 솔찍히 쓰래기 코드
    while standcnt == 0 or standcnt != cnt or stand != i:
        standcnt = cnt
        if answerMoney>=money[i]:
            answerMoney -= money[i]
            cnt += 1
            stand=i
            
        if answerMoney <= 0:
            print(cnt)
            exit()

        if standcnt == cnt :
            break



# 누군가의 깔끔한 코드    -> 횟수를 구하는 거니까 뺄샘이 아닌 몫으로 count를 샘
n, k = map(int, input().split())
value = list()

cnt = 0

for i in range(n) :
    value.append(int(input()))
value.sort(reverse = True)

for i in range(n):
    if k == 0: break
    elif k >= value[i]:
        cnt += k//value[i]
        k %= value[i] # 핵심코드

print(cnt)
