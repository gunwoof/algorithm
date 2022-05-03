from sys import stdin as s

n=int(s.readline())

for i in range(n):
    number=list(map(int,s.readline().split()))
    print(sum(number))
    number.clear()