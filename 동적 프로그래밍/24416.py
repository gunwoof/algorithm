from sys import stdin as s


def fibo(n) :
    global cnt1
    
    if n==1 or n==2:
        cnt1 += 1 # 함수 실행 횟수가 아닌 노드를 도는 횟수
        return 1
    
    return fibo(n-1)+fibo(n-2)

def fibonacci(n):
    global dp,cnt2

    dp[1],dp[2] = 1,1

    for i in range(3,n+1):
        cnt2 += 1 # 함수 실행 횟수가 아닌 노드를 도는 횟수(메모리제이션으로 인한 중복제거)
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n=int(s.readline())
dp=[0 for _ in range(n+1)] 
cnt1,cnt2=0,0

fibo(n)
fibonacci(n)
print(cnt1,cnt2)