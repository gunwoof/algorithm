from sys import stdin as s

n = int(s.readline())
number=[int(s.readline()) for i in range(n)]

for i in range(n):
    j = i
    tmp = number[j]
    while j > 0 and number[j-1]>tmp:
        number[j]= number[j-1]
        j -=1
    number[j]=tmp

for i in number:
    print(i)