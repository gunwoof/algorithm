from sys import stdin as s

M,N = map(int,s.readline().split())

for i in range(M,N+1):
    cnt=1
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j ==0 :
            cnt=0 
            break
    if cnt ==1:
        print(i)

    


    