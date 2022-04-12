'''n, m = map(int,input().split())
card = list(map(int,input().split()))
max = 0 # 비교해서 최대값으로 만들기

for i in range(n-2) : # 3번이기 때문에 3중 for문을 사용해서 완전탐색
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            sum = card[i]+card[j]+card[k]
            if sum <= m and max < sum :
                max = sum

print(max)'''


# itertools라이브러리 의 조합메소드 사용
'''from itertools import combinations as c

n, m = map(int,input().split())
card = list(map(int,input().split()))
max = 0

threeCard =list(c(card,3))
for i in range(len(threeCard)) :
    sumcard = sum(threeCard[i])
    if sumcard <=m and sumcard > max :
        max = sumcard

print(max)'''


# 재귀호출로 풀어보기
# 재귀호출 구성방법
# 1. 종료조건에서 해답을 return
# 2. 분제집합을 분할하여 재귀호출
# 3. 부분문제의 해답을 이용하여 전체문제의 해답을 return
def black(n,m,card,sn,sum=0):
    if sn == 0 :    
        return card[n-1]
    if n == 0 : 
        return 0

    if sum > m :
        return 0
    
    return sum+max(black(n-1,m,card,sn,sum),black(n-1,m,card,sn-1,sum))

print(black(5,21,[5,6,7,8,9],3,0))