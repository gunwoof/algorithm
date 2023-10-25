from sys import stdin as s

N=int(s.readline())

number=[int(s.readline()) for _ in range(N)]
number.sort()

# n이 2이상일 경우 
if N>1:
    number[0]=number[0]*(N-1)
    for i in range(1,N):
        number[i]=number[i]*(N-i)   

    print(sum(number))
else :
    print(0)



# 10 20 30 40 50 
# n-1 n-1 n-2 n-3 n-4
# (10 20) (10 20 30) (10 20 30 40) (10 20 30 40 50)
