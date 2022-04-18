from sys import stdin as s

N = int(s.readline())
distance = list(map(int,s.readline().strip().split()))
oilSt= list(map(int,s.readline().strip().split()))
cost =[]
minCost = 1000000000

for i in range(len(distance)): # 본인 위치의 주유소 보다 더 싼 주유소가 나올때 까지 본인위치의 주유소 가격만 사용하기
    if oilSt[i] < minCost:
        minCost = oilSt[i]
    
    cost.append(minCost*distance[i])

print(sum(cost))


    



