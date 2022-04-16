pn = int(input())
Pi = list(map(int,input().split()))
Pi.sort() 

sumPi = [] # 기다리는시간+자기시간을 받는 리스트
for i in range(pn) :
    if i == 0:
        sumPi.append(Pi[i])
    else :
        sumPi.append(Pi[i]+sumPi[i-1])

print(sum(sumPi))