n = int(input())
for i in range(1,n+1) :
    sum = i # 생성자가 될 수
    div = i # 각 자리를 더하기 위한 도구
    for j in range(len(str(sum))) :
        sum += div%10
        div //= 10
        
    
    if sum == n :
        print(i)
        exit()
    if i == n :
        print("0")
        exit()


# 이전에 푼 쓰래기 코드(안 돌아감) 
'''n = int(input())
i = 1
sum = 0

while  1 <= i and i <= n :
    leng = len(str(i))
    
    for j in range(1,leng) :
        sum += i//(10*j)
    sum += i+ i%10
    #print(sum)

    if sum == n :
        print(sum)
        exit()
    
    sum = 0
    i += 1

print("0")'''

