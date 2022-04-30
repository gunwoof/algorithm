from sys import stdin as s

n = int(s.readline())
number=[int(s.readline()) for i in range(n)]

for i in range(n):
    min= number[i]
    min_index = i
    for j in range(i+1,n):
        if min > number[j]:
            min = number[j]
            min_index = j
    number[i],number[min_index] = number[min_index],number[i]

for i in number:
    print(i)
