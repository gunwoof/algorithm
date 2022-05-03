from sys import stdin as s

x,y = map(int,s.readline().split())
sum=0

numbers = []
i=1   
restH=1

while len(numbers) <1000:
    number=int(str(i)*i)
    if i//10**restH == 0 : # 같은 숫자를 쪼개서 저장
        while number !=0 :
            rest = number%10**restH
            number = number//10**restH
            numbers.append(rest)
        i +=1
    else : # 자리수가 커지면 10을 더 곱해줌
        restH += 1
       
for i in range(x-1,y) :
    sum += numbers[i]
print(sum)


# 누군가의 깔끔한 코드
'''a,b=map(int,input().split())
data=[]

for i in range(1,b+1):
  for j in range(i):
    data.append(i)

print(sum(data[a-1:b]))'''

