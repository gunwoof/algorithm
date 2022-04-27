from sys import stdin as s
N = int(s.readline())
A = list(map(int,s.readline().split()))
B = list(map(int,s.readline().split()))
A.sort(reverse = True)
B.sort()

sum=0
for i in range(N):
    sum += A[i]*B[i]

print(sum)