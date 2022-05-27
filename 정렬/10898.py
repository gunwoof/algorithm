from sys import stdin as s

n = int(s.readline())
number=[0]*10000


for i in range(n):
    number[int(s.readline())] += 1

for i in range(len(number)):
    if number[i] !=0:
        for j in range(number[i]):
            print(i)
