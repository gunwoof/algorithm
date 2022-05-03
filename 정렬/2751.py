# 내장함수 사용
from sys import stdin as s
N = int(s.readline())
number=[]

for i in range(N):
    number.append(int(s.readline()))

number.sort()
for i in number:
    print(i)

