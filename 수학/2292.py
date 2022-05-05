from sys import stdin as s
N=int(s.readline())

i=1
while 1:
    if N==1:
        print(1)
        break
    elif (3*((i)**2))-(3*i)+1 <N and N<=(3*((i)**2))+(3*i)+1: 
        print(i+1)
        break
    i +=1

