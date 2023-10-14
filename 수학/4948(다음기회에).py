from sys import stdin as s

while 1:
    n=int(s.readline())
    if n == 0:
        exit()


    if n==1:
        print(2)
        continue

    prim_n_cnt=0
    for i in range(n,2*n+1):
        prim=True
        
        for j in range(2,int(i**0.5)+1):
            if i%2==0 and i != 2:
                prim=False
                break
            elif i == 2:
                break
            elif i%j == 0 :
                prim=False
        if prim == True :
            prim_n_cnt+=1

    print(prim_n_cnt)



        